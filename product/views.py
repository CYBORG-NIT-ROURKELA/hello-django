from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h1>Hello Home page</h1>")