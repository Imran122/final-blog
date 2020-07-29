from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name = 'index'),
	path('blog/<int:category>/', views.blog, name = 'category_blog'),
	path('blog/', views.blog, name = 'blog'),
	path('search/', views.search, name = 'search'),
	path('django/', views.django, name = 'django'),
	path('categorey/', views.categorey, name = 'categorey'),
	path('<slug:slug>(?P<id>\d+)/$', views.post, name='post')


]
