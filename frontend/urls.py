# -*- coding: utf-8 -*-
from django.urls import path

from . import views
urlpatterns = [
      path("", views.index, name='index'),
      path("<str:lang>", views.index, name='language'),
      path("home/<int:page_id>/", views.home, name='home'),
      path("<str:lang>/home/<int:page_id>/", views.home, name='home'),
      path('courses/', views.courses, name='courses'),
      path('<str:lang>/courses/', views.courses, name='courses'),
      path('<str:courseName>/upload/', views.upload, name = 'upload'),
      path('<str:lang>/<str:courseName>/upload/', views.upload, name = 'upload')
]