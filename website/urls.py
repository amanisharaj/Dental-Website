from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homepage'),
    path('about',views.about, name='about'),
    path('service',views.service, name='service'),
    path('pricing',views.pricing, name='pricing'),
    path('blog',views.blog, name='blog'),
    path('blogDetails',views.blogDetails, name='blogDetails'),
    path('contact',views.contact, name='contact'),
]




