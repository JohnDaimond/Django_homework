from django.contrib import admin
from django.urls import path
from .views import CartView, CartDeleteView


urlpatterns = [
    path('add/', CartView.as_view(), name="cart-add"),
    path('remove/', CartDeleteView.as_view(), name="cart-remove")
]
