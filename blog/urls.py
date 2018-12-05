from django.urls import path  # Here we're importing Django's function path and all of our views from the blog application
from . import views

urlpatterns = [
path('', views.post_list, name='post_list'),  # we're now assigning a view called post_list to the root URL
#  The last part, name='post_list', is the name of the URL that will be used to identify the view. 
]