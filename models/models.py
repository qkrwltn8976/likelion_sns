from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from PIL import Image
from image_cropping import ImageCropField, ImageRatioField

class User(AbstractUser):
	#image = ImageField(_("Image of User"), upload_to="img/", default="none/default_profile.jpg")
	relations = models.ManyToManyField(
		'self',
		symmetrical=False,
		through = 'Relation',
		related_name = '+' 
	)

class Relation(models.Model): ## 관계 정의
	RELATION_TYPE_FRIEND = 'f' ##friend 친구
	RELATION_TYPE_ACQUAINT = 'a' ##acquaintance 지인
	RELATION_TYPE_CELEB = 'c' ##celebrity 유명인사
	CHOICES_TYPE = (
		(RELATION_TYPE_FRIEND, 'friend'),
		(RELATION_TYPE_ACQUAINT, 'acqaintance'),
		(RELATION_TYPE_CELEB, 'celebrity'),
	)
	from_user = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name = 'relations_by_from_user',
	)
	to_user = models.ForeignKey(
		User,
		on_delete = models.CASCADE,
		related_name = 'relations_by_to_user',
	)
	type = models.CharField(max_length=1, choices=CHOICES_TYPE)


class Post(models.Model):
	objects = models.Manager()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	content = models.TextField()
	image = ImageCropField(upload_to = "static/images/", blank = True)
	cropping = ImageRatioField('image', '300x300')
	mark = models.ManyToManyField(User, related_name='mark')
	like = models.ManyToManyField(User, related_name='like')

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	
