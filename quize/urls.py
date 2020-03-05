"""quize1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from users import views as users_views
from quize_app import views as quize_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quize_views.home),
    path('quize/', include('quize_app.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='quize-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='quize-logout'),
    path('profile/', users_views.profile,name='quize-profile'),
    path('register/', users_views.register,name='quize-register'),
]