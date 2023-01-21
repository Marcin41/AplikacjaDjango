from rest_framework import routers
from django.urls import include, path
from .views import ActorViewSet, DirectorViewSet, MovieViewSet, RatingViewSet, RegisterAPI, LoginAPI
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r'Actors', ActorViewSet)
router.register(r'Directors', DirectorViewSet)
router.register(r'Movies', MovieViewSet)
router.register(r'Ratings', RatingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
