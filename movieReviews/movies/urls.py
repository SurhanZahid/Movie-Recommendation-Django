from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from accounts.views import (login_view , register_view , logout_view)
from django.conf import settings
from django.conf.urls.static import static
app_name = 'movies'

urlpatterns = [
    path('home', views.post_list, name='home'),
    path('login',login_view,name='login'),
    path('logout', logout_view, name='logout'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('detail/<int:id>', views.detail, name='detail')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

