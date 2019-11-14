from django.urls import path

from . import views as home_views

urlpatterns = [
    path('about/', home_views.about, name='about'),
    path('robot/', home_views.robot, name='robot'),
]
