from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# First, define your urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # This points to the home view
]

# Then add the media URL configuration
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
