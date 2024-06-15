from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerOrderViewSet

router = DefaultRouter()
router.register(r'customer-orders', CustomerOrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]

