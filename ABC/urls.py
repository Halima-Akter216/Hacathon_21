"""ABC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from Halima import views as KHL
from ORH import views as OZ
from Hackathon import views as Contest_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hal/', KHL.hal),
    path('RH/',KHL.RH),
    path('login/',OZ.Diu),
    path('Login/',Contest_url.Contest),
    path('Reg/',Contest_url.Contest_Day2),

]


