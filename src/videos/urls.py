from django.urls import path
from .views import YouTuubeVideosAPIView


urlpatterns = [
    path('lastest-youtube-videos/', YouTuubeVideosAPIView.as_view()),
    ]
