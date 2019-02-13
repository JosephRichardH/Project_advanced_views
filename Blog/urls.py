from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPost, name='Blog'),
    path('input/', views.input_post, name='input_post_blog'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.KebunBinatang, name='KebunBinatang'),
#     path('tes1/', views.tes1KebunBinatang, name='tes1KebunBinatang'),
#     path('input/', views.input_post, name='input_post'),

# ]

