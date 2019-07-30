from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from . import views

app_name = "main"
urlpatterns = [
	path('', views.home, name="home"),
	path('new_post/', views.new_post, name="new_post"),
	path('my_posts/', views.my_posts, name="my_posts"),
	path('filter/', views.filter, name="filter"),
	path('profile/<int:id>/', views.profile, name="profile"),
	path('follow/<int:id>/', views.follow, name="follow"),
	path('like_toggle/<int:id>', views.like_toggle, name="like_toggle"),
	path('detail_post/<int:id>', views.detail_post, name="detail_post"),
	path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)