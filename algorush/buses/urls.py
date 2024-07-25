from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusViewSet, RouteViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'buses', BusViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
