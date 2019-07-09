from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "random_Word/index.html")

def createWord(request):
    if request.method =="POST":
    ## this is the code for displaying and returning a random word (string of 14 characters)
        word = get_random_string(length=14)
        context = {
            "word" : word,
        }
    
    ## this is the code for displaying and returning a counter (attempt) on the index.html
    if 'attempt' in request.session:
        request.session['attempt'] += 1
    else:
        request.session['attempt'] = 1

    return render(request, "random_Word/index.html", context)

def reset(request):
    request.session.clear()
    return redirect('/')



# Create your views here.
