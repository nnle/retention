# -*- coding: utf-8 -*-
from django.contrib import admin
# Register your models here.
from .models import Navibar, Post, Course

admin.site.register(Navibar)
admin.site.register(Post)
admin.site.register(Course)