from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('core.urls')),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
    path("__reload__", include("django_browser_reload.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
