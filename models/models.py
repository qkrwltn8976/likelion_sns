from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
	#image = ImageField(_("Image of User"), upload_to="img/", default="none/default_profile.jpg")
	relations = models.ManyToManyField(
		'self',
		symmetrical=False,
		through = 'Relation',
		related_name = '+' ##related_name이 +이므로 User.+.all()하면 모델을 참조하는 모든 관계들이 나온다
	)

class Relation(models.Model): ## 관계 정의
	RELATION_TYPE_FRIEND = 'f' ##friend 친구
	RELATION_TYPE_ACQUAINT = 'a' ##acquaintance 지인
	RELATION_TYPE_CELEB = 'c' ##celebrity 유명인사
	CHOICES_TYPE = (
		(RELATION_TYPE_FRIEND, '친구'),
		(RELATION_TYPE_ACQUAINT, '지인'),
		(RELATION_TYPE_CELEB, '유명인사'),
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


#class Post(models.Model):
#	objects = models.Manager()

#	created_at = models.DateTimeField(auto_now_add=True)
#	updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
