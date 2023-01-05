from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import VideoSerializer
from .models import Video


class YouTuubeVideosAPIView(APIView):
    '''Просто для примера'''
    def get(self, request):
        return Response({'videos': []}, status=status.HTTP_200_OK)


class VideoViewSet(ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


