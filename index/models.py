from django.db import models
from django.utils import timezone


def user_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    file_name = timezone.now().strftime("%Y%m%d_%H%M%S")
    file = file_name + '.' + ext
    return 'media/users/{file}'.format(file=file)


def sites_cover_path(instance, filename):
    ext = filename.split('.')[-1]
    file_name = timezone.now().strftime("%Y%m%d_%H%M%S")
    file = file_name + '.' + ext
    return 'media/sites/{file}'.format(file=file)


class WebSite(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    ip_addr = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(auto_now=True)
    viewed_times = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)
    cover_img = models.ImageField(
        upload_to=sites_cover_path, default='images/logo.png')

    def get_right_url(self, is_internal_ip):
        if is_internal_ip:
            return self.ip_addr
        else:
            return self.url


class Post(models.Model):
    title = models.CharField(max_length=50)
    abstract = models.TextField(max_length=500)
    content = models.TextField(default='', blank=True)
    author = models.CharField(max_length=50)

    viewed_times = models.IntegerField(default=0)
    favorite = models.IntegerField(default=0)
    cover_img = models.ImageField(
        upload_to=sites_cover_path, default='images/logo.png')
    created_time = models.DateField(auto_now_add=True)
    modified_time = models.DateField(auto_now=True)


class Staff(models.Model):
    name = models.CharField(max_length=50)
    positions = models.CharField(max_length=50)
    profile = models.TextField(max_length=500)
    level = models.IntegerField(default=0)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('电话', max_length=11, null=True, blank=True)
    update_date = models.DateTimeField('最近修改时间', auto_now=True)
    avatar = models.ImageField(
        upload_to=user_avatar_path, default='images/logo.png')
