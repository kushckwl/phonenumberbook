from django.urls import path, include
from phonebook.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.ContactViewSet, basename='contact')
router.register('user', views.UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]