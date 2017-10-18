from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count']=0
    return render(request, 'index.html')

def generate(request):
    request.session['number']= get_random_string(length=14)
    request.session['count']+=1
    return redirect('/')

def reset(request):
    del request.session['number']
    del request.session['count']
    return redirect('/')
