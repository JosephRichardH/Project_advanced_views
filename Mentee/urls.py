from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenteePost, name='Mentee'),
    path('input/', views.input_post, name='input_post'),
]
