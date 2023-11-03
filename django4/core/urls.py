from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('post<int:post_id>/', show_post, name='post')
]
