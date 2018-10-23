"""Booking URLs module."""
from django.conf.urls import url

from book.booking import views

js_info_dict = {
    'packages': ('book.booking',),
}

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^upload_booking/$', views.upload_booking, name='upload_booking'),
]
