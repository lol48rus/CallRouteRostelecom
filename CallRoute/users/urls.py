"""
URL configuration for CallRoute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.index, name='user_index'),
    # path('', views.index, name='users_index'),
    path('', views.index, name='users_index'),
    #path('register', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),
    path('register', views.register, name='register'),
    # path('register', views.register_custom, name='register'),
    path('login', auth_views.LoginView.as_view(
            template_name='users/login.html'
            ), name='login'),
    path('logout', auth_views.LogoutView.as_view(
            template_name='users/logout.html'
            ), name='logout'),
    path('favorites/<int:id>', views.add_to_favorites, name='favorites'),
    path('favorite_news/', views.favorite_news, name='favorite_news'),
    path('password', views.password_update, name='password'),
]
