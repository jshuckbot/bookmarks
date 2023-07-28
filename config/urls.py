from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accountapp/", include("accountapp.urls")),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("imagesapp/", include("imagesapp.urls", namespace="imagesapp")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
