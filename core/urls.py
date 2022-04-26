from django.urls import path
from . import views
urlpatterns = [
    path('robot.txt', views.roboto_txt, name='robot_txt'),
    path('', views.frontpage, name='frontpage'),
    path('about/', views.about,name='about')
]