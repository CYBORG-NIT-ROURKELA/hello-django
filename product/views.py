from django.shortcuts import render
from .models import Product
#from django.http import HttpResponse, JsonResponse

# Create your views here.
def homepage(request):
    #return HttpResponse("<h1>Hello Home page</h1>")
    p = Product.objects.all()
    c = {
        'name': 'KJ asdvasd',
        'fruits': ['apple', 'orange', 'mango'],
        'products': p,
    }
    return render(request, 'products.html', context=c)