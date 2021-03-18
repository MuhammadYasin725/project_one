from django.contrib import admin
from django.urls import path
from blog import views

admin.site.site_header = "CODEx Administration"
admin.site.site_title = "Welcome to CODEx!"
admin.site.index_title = "Welcome To CODEx Admin"

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about', views.about, name='blog_about'),
    path('courses', views.courses, name='blog_courses'),
    path('contact', views.contact, name='blog_contact')

]
