"""Book URLs module."""

from django.conf.urls import include, patterns, url
from django.contrib import admin

from book import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Booking views
    (r'^booking/', include('book.booking.urls')),
)
