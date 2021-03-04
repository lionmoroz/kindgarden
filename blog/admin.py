from django.contrib import admin
from .models import Post
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'slug', 'date_created', ]
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

