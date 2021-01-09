from django.contrib import admin

# Register your models here.
from .models import WebSite, Post, Staff

admin.site.register(WebSite)
admin.site.register(Post)
admin.site.register(Staff)
