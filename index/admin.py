from django.contrib import admin

# Register your models here.
from .models import WebSite,Staff

admin.site.register(WebSite)
admin.site.register(Staff)