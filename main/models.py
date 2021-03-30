import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse

    

# Create your models here.

class AboutAs(models.Model):
    title = models.CharField(max_length=250, verbose_name = "Заголовок")
    description = models.TextField(verbose_name="Опис")
    video_url = models.URLField(blank=True,null=True)
    photo = models.ImageField(verbose_name="Фото", upload_to= 'about_photo', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = ("Про нас")
        verbose_name_plural = ("Про нас")
        
    def __str__(self):
        return self.title
    

class Documentation(models.Model):
    name = models.CharField(verbose_name="Імя документа", max_length=50)
    my_storage = FileSystemStorage(location = os.path.join(settings.BASE_DIR, 'documentation'))
    files = models.FileField(verbose_name="Документ" , storage=my_storage, max_length=100)
    

    class Meta:
        verbose_name = ("Документи")
        verbose_name_plural = ("Документи")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("download", kwargs={"pk": self.pk})

class GalleryCategory(models.Model):
    name = models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = ("Категорії галереї")
        verbose_name_plural = ("Категорії галереї")
         
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("photo_list_by_category", args=[self.slug])
    
class Gallery(models.Model):
    name = models.CharField(("Імя"), max_length=50)
    category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE , blank=True, null=True)
    

    class Meta:
        verbose_name = ("Галерея")
        verbose_name_plural = ("Галерея")

    def __str__(self):
        return self.name

    def image_directory_path(instance, filename):
        return 'galery_photo/{0}/{1}'.format(instance.category.slug, filename)
    photo = models.ImageField(("Фото"), upload_to=image_directory_path, height_field=None, width_field=None)
    

class ContactInfo(models.Model):
    name = models.CharField(("Повна назва"), max_length=500)
    streat = models.CharField(("Вулиця"), max_length=100)
    phone = models.CharField(("Телефон номер 1"), max_length=50, blank=True, null=True)
    phone_two = models.CharField(("Телефон номер 2"), max_length=50, blank=True, null=True)
    email = models.EmailField(("Почта"), max_length=254)
    url = models.URLField(("Google карти"), blank=True, null=True)
    

    class Meta:
        verbose_name = ("Контактні данні")
        verbose_name_plural = ("Контактні данні")

    def __str__(self):
        return self.name


class Info(models.Model):
    title = models.CharField(max_length=120, verbose_name="Заголовок" , )
    short_description = models.TextField(max_length=520, verbose_name="Деталі", blank=True, null=True)
    url_button = models.URLField(verbose_name="Посилання", max_length=200, blank=True, null=True)
    photo = models.ImageField(verbose_name="Фото", upload_to= 'info_photo', height_field=None, width_field=None, max_length=None, blank=True, null=True)

    class Meta:
        verbose_name = ("Інформаційні данні")
        verbose_name_plural = ("Інформаційні данні")


    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=300, verbose_name = 'Прізвище Імя Побатькові' )
    position = models.CharField(max_length=200, verbose_name = 'Посада')
    photo = models.ImageField(upload_to='team_photo',verbose_name="Фото" , blank=True, null=True)

    class Meta:
        verbose_name = ("Наша команда")
        verbose_name_plural = ("Наша команда")


    def __str__(self):
        return self.name