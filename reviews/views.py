from django.shortcuts import render
from django.db.models import Count, Q
from django.http import request
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Author
from django.http import HttpResponse, request
from .models import GadgetPost
# Create your views here.




def get_gadgetcategorey_count():
	queryset1 = GadgetPost.objects.values('gadgetcategories__id', 'gadgetcategories__title').annotate(Count('gadgetcategories__title'))

	return queryset1
def gadgetcategorey(request):
	most_recent = GadgetPost.objects.order_by('-timestamp')[:3]
	gadgetcategorey_count = get_gadgetcategorey_count()

	queryset1 = GadgetPost.objects.order_by('gadgetcategories')
	query = request.GET.get('q')
	if query:
		queryset1 = queryset1.filter(
			Q(title__icontains = query)
		).distinct()

	context = {

		'queryset1': queryset1,
		'most_recent': most_recent,
		'gadgetcategorey_count': gadgetcategorey_count
	}
	return render(request, 'review/gadgetcategorey.html', context)


def gadgetpost(request, gadgetcategorey = None):

	gadgetcategorey_count = get_gadgetcategorey_count()
	most_recent = GadgetPost.objects.order_by('-timestamp')[:3]
	if gadgetcategorey is None:
		post_list = GadgetPost.objects.all()
	else:
		post_list = GadgetPost.objects.filter(gadgetcategories = gadgetcategorey)

	paginator = Paginator(post_list, 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset1 = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset1 = paginator.page(1)
	except EmptyPage:
		paginated_queryset1 = paginator.page(paginator.num_pages)

	context = {
		
		'queryset1': paginated_queryset1,
		'most_recent': most_recent,
		'page_request_var': page_request_var,
		'gadgetcategorey_count': gadgetcategorey_count,
		
	}
	
	return render(request, 'review/gadget.html',context)


    


def gadgetdetails(request,slug, id): # post er alter a gadgetdetails
	
	gadgetcategorey_count = get_gadgetcategorey_count()
	#view_count = get_view_count()
	most_recent = GadgetPost.objects.order_by('-timestamp')[:3]
	gadgetpost = get_object_or_404(GadgetPost, slug=slug, id=id)
	
	#postview = PostView.objects.filter(post = id, client_ip=get_client_ip(request)).count()
	#print(postview)	

	context = {
		#'postview':postview,
		#'view_count': view_count,
		'gadgetpost': gadgetpost,
		'most_recent': most_recent,
		'gadgetcategorey_count': gadgetcategorey_count,
		
	}
	return render(request, 'review/gadgetdetails.html', context)



def gadgetsearch(request):
	most_recent = GadgetPost.objects.order_by('-timestamp')[:3]
	gadgetcategorey_count = get_gadgetcategorey_count()
	queryset1 = GadgetPost.objects.all()
	query = request.GET.get('q')

	if query:
		queryset1 = queryset1.filter(
			Q(title__icontains = query)

		).distinct()

		
	paginator = Paginator(queryset1, 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset1 = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset1 = paginator.page(1)
	except EmptyPage:
		paginated_queryset1 = paginator.page(paginator.num_pages)
	context = {
		'queryset1': queryset1,
		'most_recent': most_recent,
		'gadgetcategorey_count': gadgetcategorey_count,
		'page_request_var': page_request_var,
		'queryset1': paginated_queryset1,

	}
	return render(request, 'review/gadget_search_result.html', context)
# here is code for 
