from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet, CartItemViewSet, OrderListView


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'cart-items', CartItemViewSet, basename='cartitem')


urlpatterns = [
    path('', include(router.urls)),  
    path('orders/', OrderListView.as_view(), name='order-list'),
]


