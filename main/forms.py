from django import forms
from models.models import Post, User
from image_cropping import ImageCropWidget

class PostForm(forms.ModelForm):
	image = forms.ImageField()
	class Meta:
		model = Post
		fields = [
			'image',
			'content',
		] 
		labels = {
			'image': "이미지",
			'content': "내용",
		}
		widgets = {
			'image' : ImageCropWidget,
		}
