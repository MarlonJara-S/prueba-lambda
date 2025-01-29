from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SearchView, ArticuloViewSet

router = DefaultRouter()
router.register(r'wishlist', ArticuloViewSet, basename='wishlist')

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('', include(router.urls)),
]