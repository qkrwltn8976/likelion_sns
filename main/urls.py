from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "main"
urlpatterns = [
	path('', views.home, name="home"),
	path('new_post/', views.new_post, name="new_post"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)