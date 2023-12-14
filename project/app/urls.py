from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('orders/', orders, name='orders'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('user/<int:id>', user, name='user'),
]
