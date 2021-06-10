from django.urls import path, re_path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive_year, name='archive'),
]