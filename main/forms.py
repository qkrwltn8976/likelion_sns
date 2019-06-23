from django import forms
from models.models import Post, User

class PostForm(forms.ModelForm):
	pic = forms.ImageField()
	class Meta:
		model = Post
		fields = [
			'content',
			'pic',
		] 
		labels = {
			'content': "내용",
			'pic': "이미지"
		}
