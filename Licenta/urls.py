from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include([

        path('users/', include('users.urls')),
        path('authen/', include('authen.urls')),
        path('produs/', include('produs.urls')),
        path('about/', include('about.urls')),

    ]))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
