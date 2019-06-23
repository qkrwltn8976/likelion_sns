from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
	image = ImageField(_("Image of User"), upload_to="img/", default="none/default_profile.jpg")


class Post(models.Model):
	objects = models.Manager()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
