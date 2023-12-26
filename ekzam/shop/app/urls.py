from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.MainList.as_view(), name="main"),
    path('', include('django.contrib.auth.urls')),
    path('service/', views.ServiceList.as_view(), name="services"),
    path('service/<int:id>/', views.service_detail, name='services-detail'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('profile/', views.profile, name="profile"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
