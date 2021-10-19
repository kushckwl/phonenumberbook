from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign, name='sign'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create/', views.Create.as_view(), name='create'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('<int:pk>/update', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),
]   