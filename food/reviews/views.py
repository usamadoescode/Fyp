from django.shortcuts import render
from .models import Review
from .forms import User_Review
from django.shortcuts import get_object_or_404,redirect
# Create your views here.


def Reviews_List(request):
    reviews = Review.objects.all().order_by('-posted_on')
  
    return render(request, 'reviews/index.html',{'reviews': reviews})



def Review_created(request):
    if request.method == "POST":
        form = User_Review(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)  # Don't save to DB yet
            review.user = request.user  # Assign the current logged-in user to the review
            review.save()  # Save the review after assigning the user
            return redirect('Reviews_List')  # Redirect to the reviews list page
    else:
        form = User_Review()

    return render(request, 'reviews/Review_created.html', {'form': form})


def Review_edit(request, review_id):
    # Get the review object or return a 404 if not found or the user doesn't own it
    review = get_object_or_404(Review, pk=review_id, user=request.user)

    if request.method == "POST":
        form = User_Review(request.POST, request.FILES, instance=review)

        if form.is_valid():
            form.save()  # Save the form after assigning the current user
            return redirect('Reviews_List')  # Redirect to the reviews list page

    else:
        form = User_Review(instance=review)

    return render(request, 'reviews/Review_created.html', {'form': form})


def Review_deleted(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    
    if request.method == "POST":
        review.delete()
        return redirect('Reviews_List')  # Assuming this is the name of the URL for the reviews list

    return render(request, 'reviews/Review_deleted.html', {'review': review})
