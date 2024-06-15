from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ManufacturerViewSet, CountryViewSet, InstrumentViewSet, ItemViewSet 

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'manufacture', ManufacturerViewSet)
router.register(r'country', CountryViewSet)
router.register(r'instrument', InstrumentViewSet)
router.register(r'item', ItemViewSet)
urlpatterns = [
    path('shop/', include(router.urls))
]

