from rest_framework import routers
from django.urls import path, include
from .api import PostViewSet


router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'posts')

urlpatterns = router.urls