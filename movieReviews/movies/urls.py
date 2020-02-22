from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from accounts.views import (login_view , register_view , logout_view)
from django.conf import settings
from django.conf.urls.static import static
app_name = 'movies'

urlpatterns = [
    url(r'^home', views.post_list, name='home'),
    url(r'^login/',login_view,name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^recommendations/', views.Recommendation, name='recommendation')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

