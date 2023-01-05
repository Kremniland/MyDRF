from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from src.posts.views import PostViewSet
from src.videos.views import VideoViewSet
from src.files.views import FileViewSet

schema_view = get_swagger_view(title='MyDRF API')

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'videos', VideoViewSet, basename='videos')
router.register(r'files', FileViewSet, basename='files')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('videos/', include('src.videos.urls')),

    # path('', include(router.urls)),
]

urlpatterns += router.urls

# Для статики:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
