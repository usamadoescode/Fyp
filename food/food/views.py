from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import Restaurant,Menu



def home(request):
  
    top5_vendors = Restaurant.objects.filter(overall_rating__gte=4.5) \
                                      .order_by('-total_ratings', '-overall_rating')[:8] \
                                      .values('vendor_name', 'overall_rating', 'total_ratings', 'location')
    
    # Create the context dictionary
    context = {'top5_vendors': top5_vendors,
            
            'pages_names':{'page':'DineMap-Home', 'reviews':'Reviews'} 
               
               }  # Pass top5_vendors to the template

    # Render the home template
    return render(request, 'food/home.html', context)

def about(request):
    return render(request, 'food/about.html')


def account(request):
    return render(request, 'food/account.html')


def contact(request):
    return render(request, 'food/contact.html')




