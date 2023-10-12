from produs import models
from rest_framework import serializers
from django import forms


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banner
        fields = '__all__'


class ServiciiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servicii
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Images
        fields = '__all__'


class ProdusSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True)

    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False  # Faceți câmpul opțional pentru cererile PATCH
    )

    class Meta:
        model = models.Produs
        fields = '__all__'

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        produs = models.Produs.objects.create(**validated_data)
        for image in uploaded_images:
            models.Images.objects.create(produs=produs, image=image)
        return produs

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop("uploaded_images", [])
        for image in uploaded_images:
            models.Images.objects.create(produs=instance, image=image)
        return super().update(instance, validated_data)


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comments
        # fields = '__all__'
        fields = ['comment', 'produs', 'user_id']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = ['rating', 'produs', 'user_id']

    def create(self, validated_data):
        produs = validated_data.pop('produs')
        user = validated_data.pop('user')
        rating = models.Rating.objects.create(produs=produs, user=user, **validated_data)
        produs.update_total_rating()  # Actualizăm rating-ul total al produsului
        return rating

