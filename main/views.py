from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Count

def home(request):
	return render(request, 'main/home.html')


def new_post(request):
	##user = request.user
	form = PostForm(request.POST, request.FILES or None)
	##form.fields['user'].widget = forms.HiddenInput()
	##form.fields['user'].initial = request.user
	if request.method == "POST":
		##form = PostForm(request.POST, request.FILES or None)
		if form.is_valid():
			post = form.save(commit = False)
			post.user = request.user
			post.save()
			print("+++++++")
			return redirect('main:home')
	else:
		form = PostForm()
	return render(request, 'main/new_post.html', {'form': form})


