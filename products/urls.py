from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('create/', views.product_create, name='create'),
    path('detail/<int:pk>', views.product_detail, name='detail'),
    path('list/', views.product_list, name='list')
]
