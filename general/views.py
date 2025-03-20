from django.shortcuts import render
from django.http import HttpResponse

def ecomerce_index_view(request):
    return HttpResponse('Welcome to CN334 TA views!')

