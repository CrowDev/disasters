from django.urls import path 
from . import views 

urlpatterns = [
	path('get_concept', views.Analize.get_concept, name= 'concept'),
	path('get_data', views.Analize.get_data, name= 'data'),
]
