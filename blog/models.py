from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique = True, max_length=200)
    photo = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Новини'
        verbose_name_plural = 'Новини'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])