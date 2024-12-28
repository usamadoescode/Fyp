from django.urls import path
from . import views

urlpatterns = [
    path('', views.Reviews_List, name='Reviews_List'),  # List view for reviews
    path('Review_created/', views.Review_created, name='Review_created'),  # Create review
    path('<int:review_id>/delete/', views.Review_deleted, name='Review_deleted'),  # Delete review
    path('<int:review_id>/edit/', views.Review_edit, name='Review_edit')  # Edit review
]
