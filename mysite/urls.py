"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from blog.views import post_list
#from blog.views import home
#from blog.views import about
#from blog.views import post_detail
#from blog.views import post_create
#from blog.views import post_edit
#from blog.views import post_delete
#from blog.views import contacts
from blog import views as blog_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_views.post_list, name='post_list'),
    path('', blog_views.home, name='home'),
    path('about/', blog_views.about, name='about'),
    path('contacts/', blog_views.contacts, name='contacts'),
    path("blog/<int:pk>/", blog_views.post_detail, name="post_detail"),
    path("blog/create/", blog_views.post_create, name="post_create"),
    path("blog/<int:pk>/edit/", blog_views.post_edit, name="post_edit"),
    path("blog/<int:pk>/delete/", blog_views.post_delete, name="post_delete"),

    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")), 
    
]
