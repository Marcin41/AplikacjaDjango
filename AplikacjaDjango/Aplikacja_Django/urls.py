from rest_framework import routers
from django.urls import include, path
from .views import ActorViewSet, DirectorViewSet, MovieViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register(r'Actors', ActorViewSet)
router.register(r'Directors', DirectorViewSet)
router.register(r'Movies', MovieViewSet)
router.register(r'Ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
