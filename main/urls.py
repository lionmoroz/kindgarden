from django.urls import path , include , re_path
from .views import About , Documentation , DocumentationDownload ,GalleyView, HomeView , ContactInfo,Team

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('doc/', Documentation.as_view(), name = 'document' ),
    path('', HomeView.as_view(), name='home'),
    re_path(r'^download/(?P<pk>[0-9]+)/$', DocumentationDownload.as_view(), name='download'),
    path('gallery/' , GalleyView.as_view() ,name='photo_list'),
    path('contact/', ContactInfo.as_view(), name='contact' ),
    path('team/', Team.as_view(), name='team'),
]