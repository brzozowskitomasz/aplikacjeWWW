"""biblioteka URL Configuration

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
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from biblioteka1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^autorzylista/', views.Autorzylista.as_view()),
    url(r'^wypozyczenia/', views.wypozyczenial.as_view()),
    url(r'^kategorie/', views.kategoriel.as_view()),
    url(r'^wydawnictwo/', views.wydawnictwol.as_view()),
    url(r'^ksiazki/', views.ksiazkil.as_view()),
    url(r'^czytelnicy/', views.czytelnicyl.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
