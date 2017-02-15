from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.otp_register, name='register'),
    url(r'^login/$', views.otp_login, name='login'),
    url(r'^verify/$', views.otp_verify, name='verify'),
    url(r'^status/$', views.otp_status, name='status'),
    url(r'^logout/$', views.otp_logout, name='logout'),
    url(r'^token/$', views.otp_token, name='token'),
]