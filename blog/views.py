from django.shortcuts import render

posts = [
	{
		'author': 'Jack',
		'title': 'Review 1',
		'content': 'First review content',
		'date_posted': 'December 25, 2019'
	},
		{
		'author': 'Xai',
		'title': 'Review 2',
		'content': 'Second review content',
		'date_posted': 'December 26, 2019'
	}

]

def home(request):	
	# create dictionary
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

