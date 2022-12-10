from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='ip'),
    path('ip/', views.show_ip, name='ip'),
    path('ips/', views.show_ips, name='ips'),
    path('api/ip=<str:ip>', views.show_ip_args),
    path('api/ips/', views.show_ips_args),
    path('about/', views.about, name='about'),
]

