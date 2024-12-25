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

       form= User_Review(request.POST,request.FILES)
       Review = form.is_valid(commit=False)
       Review.user  = redirect.user
       Review.save()
       return redirect('Reviews_List')
    else:
        form = User_Review()
        return render(request , 'review_form.html', {'form': form})
    


