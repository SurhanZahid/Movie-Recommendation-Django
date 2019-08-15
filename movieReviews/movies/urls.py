from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'movies'

urlpatterns = [
    url(r'^home', views.post_list, name='home'),
    url(r'^recommendations/', views.Recommendation, name='recommendation')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

