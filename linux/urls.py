from django.urls import path
from . import views
urlpatterns = [
    path('linuxsearch/', views.linuxsearch, name = 'linuxsearch'),	
    path('linuxpost/<int:linuxcategorey>/', views.linuxpost, name = 'linuxcategorey_linuxpost'),
	path('linuxpost/', views.linuxpost, name = 'linuxpost'),
	path('linuxcategorey/', views.linuxcategorey, name = 'linuxcategorey'),
	path('<slug:slug>(?P<id>\d+)/$', views.linuxdetails, name = 'linuxdetails'),
]