"""library URL Configuration

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
from django.urls import path,include

from .api import router
from api.views import BookCatelogyListView,BookCatelogyListCreate, BookCatelogyListCreateView,BookCatelogyRetrieveView,BookCatelogyUpdateView,BookCatelogyUpdateRetrieveView,BookCatelogyDestroyView
urlpatterns = [
    path('admin/', admin.site.urls),
    #api faylarimizni urls qushib quyamiz
    path('',include(router.urls)),
]


urlpatterns += [
    path('category-list/', BookCatelogyListView.as_view()),
    path('category-craete/', BookCatelogyListCreate.as_view()),
    path('category-listcraete/', BookCatelogyListCreateView.as_view()), 
    path('category-retrieve/<int:pk>', BookCatelogyRetrieveView.as_view()),
    path('category-update/<int:pk>', BookCatelogyUpdateView.as_view()),
    path('category-retrieve-update/<int:pk>', BookCatelogyUpdateRetrieveView.as_view()),
    path('category-delete/<int:pk>', BookCatelogyDestroyView.as_view()), 
]