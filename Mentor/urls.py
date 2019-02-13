from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorPost, name='Mentor'),
    path('input/', views.input_post, name='input_post'),
]
