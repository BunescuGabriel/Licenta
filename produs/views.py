from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import Http404
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Banner, Produs, Comments, Rating
from .serializers import BannerSerializer, ProdusSerializer, CommentsSerializer, RatingSerializer
from PIL import Image
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from users.models import UserToken
from rest_framework.exceptions import PermissionDenied
import django_filters
from django_filters import rest_framework as filters
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings


class CreateBanner(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        name_banner = data.get('name_banner')
        banner = data.get('banner')

        if banner is not None:
            try:
                img = Image.open(banner)
                if img.format not in ('JPEG', 'PNG'):
                    return Response({'banner': 'Invalid image format'}, status=status.HTTP_400_BAD_REQUEST)
                # if img.width > 10000 or img.height > 10000:
                #     return Response({'banner': 'Image dimensions are too large'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'banner': 'Invalid image'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(
            name_banner=name_banner,
            banner=banner
        )


class DeleteBanner(generics.RetrieveDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user

        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("Nu puteți șterge bannere după ce ați făcut logout.")

            # Verificați dacă utilizatorul are is_superuser mai mare ca 0
            if user.is_superuser > 0:
                instance.delete()  # Șterge banner-ul
            else:
                raise PermissionDenied("Nu aveți permisiunea de a șterge bannere.")

        except UserToken.DoesNotExist:
            raise PermissionDenied("User token does not exist or has been deleted.")

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Banner.DoesNotExist:
            raise Http404


class ProdusFilter(django_filters.FilterSet):
    producator = django_filters.ChoiceFilter(
        choices=Produs.objects.order_by('producator').values_list('producator', 'producator').distinct()
    )
    cutia = django_filters.ChoiceFilter(
        choices=Produs.objects.order_by('cutia').values_list('cutia', 'cutia').distinct()
    )
    motor = django_filters.ChoiceFilter(
        choices=Produs.objects.order_by('motor').values_list('motor', 'motor').distinct()
    )
    numar_usi = django_filters.ChoiceFilter(
        choices=Produs.objects.order_by('numar_usi').values_list('numar_usi', 'numar_usi').distinct()
    )
    numar_pasageri = django_filters.ChoiceFilter(
        choices=Produs.objects.order_by('numar_pasageri').values_list('numar_pasageri', 'numar_pasageri').distinct()
    )
    caroserie = django_filters.ChoiceFilter(
        choices=Produs.objects.order_by('caroserie').values_list('caroserie', 'caroserie').distinct()
    )
    an = django_filters.RangeFilter(label='An între')
    capacitate_cilindrica = django_filters.RangeFilter(label='Capacitate Cilindrica între')

    class Meta:
        model = Produs
        fields = [
        'producator',
        'cutia',
        'motor',
        'numar_usi',
        'numar_pasageri',
        'caroserie',
        'an',
        'capacitate_cilindrica',
        ]


class ListProdus(generics.ListAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProdusFilter


class CreateProdus(ListCreateAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user

        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("Nu puteți crea car după ce ați făcut logout.")

            # Verificați dacă utilizatorul are is_superuser mai mare ca 0
            if user.is_superuser > 0:
                return super().create(request, *args, **kwargs)
            else:
                raise PermissionDenied("Nu aveți permisiunea de a crea car.")

        except UserToken.DoesNotExist:
            raise PermissionDenied("User token does not exist or has been deleted.")

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Produs.DoesNotExist:
            raise Http404


class UpdatePartialProdus(RetrieveUpdateAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class UpdateProdus(RetrieveUpdateDestroyAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        user = self.request.user

        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("You cannot delete a rating after logging out.")

            if user.is_superuser:
                serializer = self.get_serializer(instance, data=request.data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied("You do not have permission to delete a rating.")

        except UserToken.DoesNotExist:
            raise PermissionDenied("User token does not exist or has been deleted.")

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404


class DeleteProdus(generics.RetrieveDestroyAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def perform_destroy(self, instance):
        user = self.request.user

        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("Nu puteți șterge rating după ce ați făcut logout.")

            if user.is_superuser > 0:
                instance.images.all().delete()
                instance.delete()
            else:
                raise PermissionDenied("Nu aveți permisiunea de a șterge rating.")

        except UserToken.DoesNotExist:
            raise PermissionDenied("User token does not exist or has been deleted.")

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except ObjectDoesNotExist:
            raise Http404


class AddCommentView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("Nu puteți adăuga comentarii după ce ați făcut logout.")
            serializer.save(user=user)
        except UserToken.DoesNotExist:
            raise PermissionDenied("Utilizatorul nu există sau a fost șters.")


class DeleteGetCommentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user

        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("Nu puteți șterge comentariul după ce ați făcut logout.")

            # Verificați dacă utilizatorul are is_superuser mai mare ca 0
            if user.is_superuser > 0:
                instance.delete()  # Șterge banner-ul
            else:
                raise PermissionDenied("Nu aveți permisiunea de a șterge comentariul.")

        except UserToken.DoesNotExist:
            raise PermissionDenied("User token does not exist or has been deleted.")

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Comments.DoesNotExist:
            raise Http404


class ProductCommentsView(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']

        return Comments.objects.filter(produs_id=product_id)


class CreateRatingView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        user_token = UserToken.objects.filter(user=user).first()
        if user_token and user_token.logout_time is not None:
            raise PermissionDenied("Nu puteți adăuga rating după ce ați făcut logout.")

        #
        produs = serializer.validated_data.get('produs')
        existing_rating = Rating.objects.filter(user=user, produs=produs).first()
        if existing_rating:
            existing_rating.rating = serializer.validated_data['rating']
            existing_rating.save()
        else:
            serializer.save(user=user)


class GetUserRatingView(generics.RetrieveAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()

    def get_object(self):
        user = self.request.user
        user_token = UserToken.objects.filter(user=user).first()
        if user_token and user_token.logout_time is not None:
            raise PermissionDenied("Nu puteți adăuga rating după ce ați făcut logout.")
        produs_id = self.kwargs['produs_id']
        return Rating.objects.filter(user=user, produs_id=produs_id).first()


class DeleteRatingView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user

        try:
            user_token = UserToken.objects.get(user=user)
            if user_token.logout_time is not None:
                raise PermissionDenied("Nu puteți șterge rating după ce ați făcut logout.")

            # Verificați dacă utilizatorul are is_superuser mai mare ca 0
            if user.is_superuser > 0:
                instance.delete()  # Șterge banner-ul
            else:
                raise PermissionDenied("Nu aveți permisiunea de a șterge rating.")

        except UserToken.DoesNotExist:
            raise PermissionDenied("User token does not exist or has been deleted.")

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Rating.DoesNotExist:
            raise Http404


class ProductRatingsView(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']

        return Rating.objects.filter(produs_id=product_id)



@csrf_exempt
def reservation_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prenume = data.get("prenume", "")
            virsta = data.get("virsta", "")
            phone = data.get("phone", "")
            fromDate = data.get("fromDate", "")
            toDate = data.get("toDate", "")
            carInfo = data.get("carInfo", {})

            car_id = carInfo.get("id", "")
            car_name = carInfo.get("name", "")
            car_producer = carInfo.get("producator", "")

            totalDays = data.get("totalDays", "")
            priceForTotalDays = data.get("priceForTotalDays", "")
            Pret_final = data.get("Pret_final", "")

            message = (
                f'Rezervarea Masinilor:'
                f'\nNume: {prenume}\nVîrsta: {virsta} ani\nTelefon: {phone}'
                f'\nDe la: {fromDate}\nPână la: {toDate}\n\nDetalii produs:'
                f'\nNume Produs: {car_producer} {car_name}'
                f'\nNumăr total de zile: {totalDays}\nPreț pentru o zi: {priceForTotalDays} €'
                f'\nPreț total: {Pret_final} €'
            )

            send_mail(
                f'Rezervarea Masinilor: mesaj nou de la {prenume}',
                message,
                virsta,
                [settings.EMAIL_HOST_USER],  # Recipient's email address
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'error': 'Metoda incorectă. Se așteaptă o cerere POST.'})


