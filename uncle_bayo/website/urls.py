from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('work', views.works, name='work'),
    path('contact-us', views.contact, name='contact'),
    path('add-work', views.create_work, name='add-work')
]
