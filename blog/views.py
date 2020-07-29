from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, request
from .models import Post, Author, Categorey, PostView
from marketing.models import Signup
from django.db.models import Count, Q
from django.db import models


# Create your views here.

def search(request):
	most_recent = Post.objects.order_by('-timestamp')[:3]
	categorey_count = get_categorey_count()
	queryset = Post.objects.all()
	query = request.GET.get('q')

	if query:
		queryset = queryset.filter(
			Q(title__icontains = query)

		).distinct()
	paginator = Paginator(queryset, 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)
	context = {
		'queryset': queryset,
		'most_recent': most_recent,
		'categorey_count': categorey_count,
		'page_request_var': page_request_var,
		'queryset': paginated_queryset,

	}
	return render(request, 'pages/search_result.html', context)
	


def get_categorey_count():
	queryset = Post.objects.values('categories__id', 'categories__title').annotate(Count('categories__title'))

	return queryset


def index(request):
	categorey_count = get_categorey_count()
	featured = Post.objects.filter(featured = True)
	latest = Post.objects.order_by('-timestamp')[0:3]
	

	
	if request.method == "POST":
		email = request.POST["email"]
		new_signup = Signup()
		new_signup.email = email
		new_signup.save()

	context = {
		'object_list': featured,
		'latest': latest,
		'categorey_count': categorey_count,
	}
	return render(request, 'pages/index.html', context)



def blog(request, category = None):

	categorey_count = get_categorey_count()
	most_recent = Post.objects.order_by('-timestamp')[:3]
	if category is None:
		post_list = Post.objects.all()
	else:
		post_list = Post.objects.filter(categories = category)

	paginator = Paginator(post_list, 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		
		'queryset': paginated_queryset,
		'most_recent': most_recent,
		'page_request_var': page_request_var,
		'categorey_count': categorey_count,
		
	}
	return render(request, 'pages/blog.html', context)



def post(request,slug, id):
	#return HttpResponse(get_client_ip(request))
	categorey_count = get_categorey_count()
	#view_count = get_view_count()
	most_recent = Post.objects.order_by('-timestamp')[:3]
	post = get_object_or_404(Post, slug=slug, id=id)
	
	postview = PostView.objects.filter(post = id, client_ip=get_client_ip(request)).count()
	print(postview)	


	
	if postview == 0:
		new_post_view = PostView()
		new_post_view.view_count = 1
		
		new_post_view.client_ip = get_client_ip(request)
		new_post_view.post = post
		new_post_view.save()
		

	view_count = PostView.objects.values('post_id').annotate(post_view=models.Count('post_id'))
		
	
	

	context = {
		'postview':postview,
		'view_count': view_count,
		'post': post,
		'most_recent': most_recent,
		'categorey_count': categorey_count,
		
	}
	return render(request, 'pages/post.html', context)


def categorey(request):
	most_recent = Post.objects.order_by('-timestamp')[:3]
	categorey_count = get_categorey_count()

	queryset = Post.objects.order_by('categories')
	query = request.GET.get('q')
	if query:
		queryset = queryset.filter(
			Q(title__icontains = query)
		).distinct()

	context = {

		'queryset': queryset,
		'most_recent': most_recent,
		'categorey_count': categorey_count
	}
	return render(request, 'pages/categorey.html', context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

#aikahen django id dhore recent,all post show er kaj korsi,
#live korar somoy kheayl rekhe database id hisabe aikhane change kore dilei hobe
def django(request):
	categorey_count = get_categorey_count()
	most_recent = Post.objects.filter(categories__id =2).order_by('-timestamp')[0:3] 
	#db te dhekbo django categorey er id koto & seta aikhane bosabo
	post_list = Post.objects.filter(categories__id =2)
	context = {
		'most_recent':most_recent,
		'categorey_count':categorey_count,
		'post_list': post_list
	}
	return render(request, 'pages/django.html',context)