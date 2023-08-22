from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact-us", views.identity_view, name='contact-us'),
    path("hospital",views.hospital,name='hospital'),
    path("township",views.township,name='township'),
    path("shopping",views.shopping,name='shopping'),
    path("refinery",views.refinery,name='refinery'),
    path("canteen",views.canteen,name='canteen'),
    path("school",views.school,name='school'),
    path("transport",views.transport,name='transport'),
    path("furniture",views.furniture,name='furniture'),
    path("office",views.office,name='office'),
    path("others",views.others,name='others'),
    path("identity_view",views.identity_view,name='confirm'),
]