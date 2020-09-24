from django.urls import path
from trafficapp import views

app_name = 'trafficapp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('admin/dashboard/', views.admindashboard, name='admindashboard'),
    path('admin/packages/', views.adminpackages, name='adminpackages'),
    path('admin/orders/', views.ordersplaced, name='ordersplaced'),
    path('admin/users/', views.userlist, name='userlist'),
    path('user/dashboard/', views.userdashboard, name='userdashboard'),
    path('user/packages/', views.userpackages, name='userpackages'),
    path('user/placeorder/', views.placeorder, name='placeorder'),
    path('user/history/', views.history, name='history'),
    path('traffic_request/', views.traffic_request, name='traffic_request'),
    path('generate_traffic/', views.generate_traffic, name='generate_traffic'),
]