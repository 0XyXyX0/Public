from django.urls import path
from .views import index, user_info

urlpatterns = [
    path('', index),
    path('user/', user_info)
]