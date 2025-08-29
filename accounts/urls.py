from django.urls import path
from .views import hello_world, register_user, get_items, delete_items, freight_order_list, freight_order_detail
from rest_framework.routers import DefaultRouter




urlpatterns = [
    path('hello/', hello_world),
    path("register/", register_user),
    path("data/", get_items),
    path("delete/<int:pk>/", delete_items),

    path('freight-orders/', freight_order_list, name='freight_order_list'),
    path('freight-orders/<int:pk>/', freight_order_detail, name='freight_order_detail'),
]