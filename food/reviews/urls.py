from . import views
from django.urls import path

urlpatterns = [
    path('', views.Reviews_List, name='Reviews_List'),
]
