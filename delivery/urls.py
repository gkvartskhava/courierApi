from rest_framework.routers import DefaultRouter
from .views import CustomUserViewset,ParcelViewset, DeliveryProofViewset
from django.urls import path, include

router = DefaultRouter()


router.register(r'users',CustomUserViewset)
router.register(r'parcels',ParcelViewset)
router.register(r'delivery_proof',DeliveryProofViewset)


urlpatterns = [
    path('api/',include(router.urls)),
]