from django.db import models

from core.models import BaseModel, BaseImage


class Post(BaseModel):
    '''Мои посты наследуем от нашего кастомного класса'''
    title = models.CharField(max_length=256, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class PostImage(BaseImage):
    '''Картинки к постам наследуем от нашего кастомного класса'''
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)


