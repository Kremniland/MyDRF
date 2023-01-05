from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Post, PostImage


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        exclude = []


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
