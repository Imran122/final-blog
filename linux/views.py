from django.shortcuts import render
from django.db.models import Count, Q
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Author
from django.http import HttpResponse, request
from .models import LinuxPost
# Create your views here.
def get_linuxcategorey_count():
	queryset2 = LinuxPost.objects.values('linuxcategories__id', 'linuxcategories__title').annotate(Count('linuxcategories__title'))

	return queryset2


def linuxcategorey(request):
	most_recent = LinuxPost.objects.order_by('-timestamp')[:3]
	linuxcategorey_count = get_linuxcategorey_count()

	queryset2 = LinuxPost.objects.order_by('linuxcategories')
	query = request.GET.get('q')
	if query:
		queryset2 = queryset2.filter(
			Q(title__icontains = query)
		).distinct()

	context = {

		'queryset2': queryset2,
		'most_recent': most_recent,
		'linuxcategorey_count': linuxcategorey_count
	}
	return render(request, 'linux/linuxcategorey.html', context)



def linuxpost(request, linuxcategorey = None):

	linuxcategorey_count = get_linuxcategorey_count()
	most_recent = LinuxPost.objects.order_by('-timestamp')[:3]
	if linuxcategorey is None:
		post_list = LinuxPost.objects.all()
	else:
		post_list = LinuxPost.objects.filter(linuxcategories = linuxcategorey)

	paginator = Paginator(post_list, 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset2 = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset2 = paginator.page(1)
	except EmptyPage:
		paginated_queryset2 = paginator.page(paginator.num_pages)

	context = {
		
		'queryset2': paginated_queryset2,
		'most_recent': most_recent,
		'page_request_var': page_request_var,
		'linuxcategorey_count': linuxcategorey_count,
		
	}
	
	return render(request, 'linux/linux.html',context)



def linuxdetails(request,slug, id): # post er alter a gadgetdetails
	
	linuxcategorey_count = get_linuxcategorey_count()
	#view_count = get_view_count()
	most_recent = LinuxPost.objects.order_by('-timestamp')[:3]
	linuxpost = get_object_or_404(LinuxPost, slug=slug, id=id)
	
	#postview = PostView.objects.filter(post = id, client_ip=get_client_ip(request)).count()
	#print(postview)	

	context = {
		#'postview':postview,
		#'view_count': view_count,
		'linuxpost': linuxpost,
		'most_recent': most_recent,
		'linuxcategorey_count': linuxcategorey_count,
		
	}
	return render(request, 'linux/linuxdetails.html', context)



def linuxsearch(request):
	most_recent = LinuxPost.objects.order_by('-timestamp')[:3]
	linuxcategorey_count = get_linuxcategorey_count()
	queryset2 = LinuxPost.objects.all()
	query = request.GET.get('q')

	if query:
		queryset2 = queryset2.filter(
			Q(title__icontains = query)

		).distinct()
	
	paginator = Paginator(queryset2, 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset2 = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset2 = paginator.page(1)
	except EmptyPage:
		paginated_queryset2 = paginator.page(paginator.num_pages)
	context = {
		'queryset2': queryset2,
		'most_recent': most_recent,
		'linuxcategorey_count': linuxcategorey_count,
		'page_request_var': page_request_var,
		'queryset2': paginated_queryset2,

	}
	return render(request, 'linux/linux_search_result.html', context)