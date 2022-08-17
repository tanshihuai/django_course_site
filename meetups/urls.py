from django.urls import path
from . import views


urlpatterns = [
    path('meetups/', views.index),
    path('meetups/success', views.confirm_registration, name='thisisaname_in_url_py_for_confirm_registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_details)
]
