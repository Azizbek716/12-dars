from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('create/', views.create_products, name='create'),
    path('category/<str:category>', views.products_by_category, name='category'),
    path('detail/<int:pk>', views.products_detail, name='detail')
]
