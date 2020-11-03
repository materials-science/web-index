from django.db import models

class WebSite(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    cover_img_url = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    start_date = models.DateField(auto_now=True)
    viewd_times = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)

class Staff(models.Model):
    name = models.CharField(max_length=50)
    positions = models.CharField(max_length=50)
    profile = models.TextField(max_length=250)
    avatar_url = models.CharField(max_length=250)
    level = models.IntegerField(default=0)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('电话',max_length=11,null=True, blank=True)
    update_date = models.DateTimeField('最近修改时间',auto_now=True)