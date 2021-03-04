from django.shortcuts import render ,get_object_or_404
from django.views.generic import TemplateView,ListView,View
from .models import AboutAs, Documentation , GalleryCategory , Gallery , Info , ContactInfo, Team
import random
from blog.models import Post
from django_downloadview import ObjectDownloadView
# Create your views here.

class About(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = AboutAs.objects.all()
        return context

class DocumentationDownload(ObjectDownloadView):
    model = Documentation
    file_field = 'files'


class Documentation(ListView):
    model = Documentation
    template_name = 'main/documentation.html'
    context_object_name = 'doc'

class Team(ListView):
    model = Team
    template_name = 'main/team.html'
    context_object_name = 'team'


class GalleyView(TemplateView):
    template_name = 'main/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_gallery = Gallery.objects.all()
        all_category = GalleryCategory.objects.all()
        context['all_gallery'] = all_gallery
        context['all_category'] = all_category
        return context     


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = AboutAs.objects.all()
        context['random_post'] = random.sample(list(Post.objects.all()), 4)
        context['info'] = Info.objects.all()
        context['about'] = AboutAs.objects.all()
        return context
from .models import ContactInfo as Contact

class ContactInfo(TemplateView):
    template_name = 'main/contact.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_info"] = Contact.objects.all()
        return context
    