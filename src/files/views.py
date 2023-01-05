from rest_framework import viewsets

from .models import File
from .serializers import FileSerializer
from core.permissions import IsSubscriber


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    Файл сохраняется рядом с папкой проекта в папке media,
    permission для пользователей из группы subscribers,
    которую мы создаем сами
    '''
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsSubscriber]


