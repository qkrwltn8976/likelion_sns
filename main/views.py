from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from models.models import *
from django.db.models import Count
from django.contrib.staticfiles.templatetags.staticfiles import static

def home(request):
	if request.user.is_active:
		posts = Post.objects.exclude(
			user = request.user
		)
	else:
		posts = Post.objects.all()
	return render(request, 'main/home.html', {'posts': posts})


def filter(request):
	user = request.user
	posts = Post.objects.exclude(
		user = request.user
	)
	
	if request.method == "POST":
		filter_type = request.POST['action']
		if filter_type == 'all':
			posts = Post.objects.exclude(
				user = request.user
			)
		else:	
			if filter_type == 'friend':
				t='f'
			elif filter_type == 'acquaintance':
				t='a'
			elif filter_type == 'celebrity':
				t='c'

			ulist_pk = user.relations_by_from_user.filter(type=t).values_list('to_user') ##사용자가 친구로 설정한 유저 pk 리스트
			ulist = User.objects.filter(pk__in=ulist_pk)
			for u in ulist:
				print(u.username)
			posts = Post.objects.exclude(
				user = request.user
			).filter(
				user__in=[u for u in ulist]
			)
	return render(request, 'main/home.html', {'posts': posts})

def new_post(request):
	if request.user.is_active:
		form = PostForm(request.POST, request.FILES or None)
		##form.fields['user'].widget = forms.HiddenInput()
		##form.fields['user'].initial = request.user
		if request.method == "POST":
			##form = PostForm(request.POST, request.FILES or None)
			if form.is_valid():
				post = form.save(commit = False)
				post.user = request.user
				post.save()
				return redirect('main:home')
		else:
			form = PostForm()
		return render(request, 'main/new_post.html', {'form': form})
	else:
		return redirect('account_login')

def my_posts(request):
	if request.user.is_active:
		posts = Post.objects.filter(
			user = request.user
		)
		return render(request, 'main/my_posts.html', {'posts': posts})
	else:
		return redirect('account_login')


def profile(request, id):
	user = request.user
	selected_user = get_object_or_404(User, pk=id)
	star_url1=""
	star_url2=""
	star_url3=""
	
	if Relation.objects.filter(from_user=user, to_user=selected_user, type='f').exists():
		star_url1 = str("images/star_1.png")
		print("++++++"+star_url1)
	else:
		star_url1 = str("images/star_2.png")
		print("-----"+star_url1)
	if Relation.objects.filter(from_user=user, to_user=selected_user, type='a').exists():
		star_url2 = str("images/star_1.png")
	else:
		star_url2 = str("images/star_2.png")
	if Relation.objects.filter(from_user=user, to_user=selected_user, type='c').exists():
		star_url3 = str("images/star_1.png")
	else:
		star_url3 = str("images/star_2.png")
	posts = Post.objects.filter(
		user = selected_user
	)
	return render(request, 'main/profile.html', context = {'posts': posts, 'user': selected_user, 'star_url1':static(star_url1), 'star_url2':static(star_url2), 'star_url3':static(star_url3)})


def follow(request, id):
	if request.user.is_active:
		user = request.user
		selected_user = get_object_or_404(User, pk=id)
		if request.method == "POST":
			t = ''
			if request.POST['type'] == "friend":
				t = 'f'
			elif request.POST['type'] == "acquaintance":
				t = 'a'
			elif request.POST['type'] == "celebrity":
				t = 'c'
			if Relation.objects.filter(from_user=user, to_user=selected_user, type=t).exists():
				r = Relation.objects.filter(from_user=user, to_user=selected_user, type=t)
				r.delete()
			else:
				Relation.objects.create(from_user=user, to_user=selected_user, type=t)
		return redirect('main:profile', selected_user.id)
	else:
		return redirect('account_login')


def like_toggle(request, id):
	if request.user.is_active:
		post = get_object_or_404(Post, pk=id)
	    # 요청한 사용자
		user = request.user

	    # 사용자의 like_posts목록에서 like_toggle할 Post가 있는지 확인
		filtered_like_posts = user.like.filter(pk=id)
	    # 존재할경우, like_posts목록에서 해당 Post를 삭제
		if filtered_like_posts.exists():
			user.like.remove(post)
	    # 없을 경우, like_posts목록에 해당 Post를 추가
		else:
			user.like.add(post)

		return redirect('main:detail_post', id)
	else:
		return redirect('account_login')


def detail_post(request, id):
	post = get_object_or_404(Post, pk=id)
	return render(request, 'main/detail_post.html', {'post': post})

