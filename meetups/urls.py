from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='meetups-index'),
    path('meetups/<slug:meetup_slug>',views.meetup_details,name='meetups-details'),
]