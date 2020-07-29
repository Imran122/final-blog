from django.urls import path
from . import views


urlpatterns = [

	path('gadgetsearch/', views.gadgetsearch, name = 'gadgetsearch'),
	path('gadgetpost/<int:gadgetcategorey>/', views.gadgetpost, name = 'gadgetcategorey_gadgetpost'),
	path('gadgetpost/', views.gadgetpost, name = 'gadgetpost'),
	path('gadgetcategorey/', views.gadgetcategorey, name = 'gadgetcategorey'),
	path('<slug:slug>(?P<id>\d+)/$', views.gadgetdetails, name = 'gadgetdetails'),
]