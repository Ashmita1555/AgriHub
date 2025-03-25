from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('agromart/', views.agro_mart, name='agro_mart'),
    path('create_business/', views.create_business, name='create_business'),
    path('create_farmer/', views.create_farmer, name='create_farmer'),
    path('community/', views.community, name='community'),
    path('create_community_post/', views.create_community_post, name='create_community_post'),
     path('test/', views.test_page, name='test')
]
