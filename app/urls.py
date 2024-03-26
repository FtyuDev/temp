from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', Base.as_view(), name='aboutit'),
    path('<str:sinf>/', CategoryView.as_view(), name='category'),
    path('<str:sinf>/<str:sinfnom>/', SinfView.as_view(), name='fanlar'),
    path('<str:sinfi>/<str:sinfnom>/<str:kun>', ProView.as_view(), name='fanlar'),
    path('about', Malumot.as_view(), name='nima'),
    path('detail', members, name='m')
]
