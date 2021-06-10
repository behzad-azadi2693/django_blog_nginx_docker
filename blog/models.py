from config.settings import STATIC_URL
from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'آماده انتشار'),
        ('published', 'انتشار')
    )
    titlle = models.CharField(max_length=60, verbose_name='تایتل')
    slug = models.SlugField(max_length=100, verbose_name='اسلاگ')
    body = models.TextField(verbose_name='پیام')
    publish = jmodels.jDateTimeField(default= timezone.now, verbose_name='تاریخ انتشار')
    created = jmodels.jDateTimeField(auto_now_add= True, verbose_name='تاریخ ایجاد')
    updated = jmodels.jDateTimeField(auto_now= True, verbose_name='تاریخ آپدیت')
    status = models.CharField(max_length=60, choices= STATUS_CHOICES, default= 'draft', verbose_name='وضعیت')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
    def __str__(self):
        return self.titlle

