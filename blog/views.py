from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
# The dot before models means current directory or current application.
# Both views.py and models.py are in the same directory. 
# This means we can use . and the name of the file (without .py). 
# Then we import the name of the model (Post).
from .forms import PostForm

from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
# We created a function (def) called post_list that takes request and will return the
# value it gets from calling another function render that will render (put together) 
# our template blog/post_list.html.

# In the render function we have one parameter request (everything we receive from the user 
# svia the Internet) and another giving the template file ('blog/post_list.html'). 
# The last parameter, {}, is a place in which we can add some things for the template to use. 
# We need to give them names (we will stick to 'posts' right now). :) 
# It should look like this: {'posts': posts}. 
# Please note that the part before : is a string; you need to wrap it with quotes: ''.
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

# Defining view to add a menu.html
def about(request):
	return render(request, 'blog/about.html', {'post':post})

# Defining view to add a post
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:	
		form = PostForm()
		return render(request, 'blog/post_edit.html', {"form":form})

#To create a new Post form, we need to call PostForm() and pass it to the template. 
# We will go back to this view, but for now, let's quickly create a template for the form.
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})