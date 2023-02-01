from rest_framework.routers import DefaultRouter 
from .views import AddressViewSet
from .views import GamesViewSet
from django.urls import path, include
router = DefaultRouter()

router.register('/address', AddressViewSet)
router.register('/games', GamesViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]