from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import AboutAs , Gallery , Documentation ,GalleryCategory,Info,ContactInfo,Team

# Register your models here.






@admin.register(GalleryCategory)
class GalleryCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(AboutAs)
class AdminAboutAs(admin.ModelAdmin):
    list_display = ['title', 'photo', ]
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
@admin.register(Documentation)
class AdminDocumentation(admin.ModelAdmin):
    list_display = ['name', 'files', ]

@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    list_display = ['name', 'category','photo', ]
    
    list_filter =['category',]

@admin.register(Info)
class AdminInfo(admin.ModelAdmin):
    list_display = ['title', 'url_button',]

@admin.register(ContactInfo)
class AdminContactInfo(admin.ModelAdmin):
    list_display = ['name', 'streat',]    

@admin.register(Team)
class AdminTeamInfo(admin.ModelAdmin):
    list_display = ['name', 'position',]   