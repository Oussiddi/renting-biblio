from django.shortcuts import render
from store.models import Book
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.http import HttpResponseRedirect
import datetime
import uuid
from store.models import BookCopy

def frontpage(request):
    return render(request,'core/frontpage.html')

def List_Books(request) :
    book = Book.objects.all() 
    return render(request, 'core/List_Books.html',{'book' : book})

def about(request) :
    list_copies = ['looking for alaska', 'paper towns', 'harry potter']
    list_prices = [20, 45, 86]
    data = {}
    
    data['books'] = list_copies
    data['prices']= list_prices
    data['books_prices'] = zip(list_copies, list_prices)
    
    return render(request, 'core/about.html', data)



def contact(request):
    submitted=False
    if request.method =='POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm    
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'core/contact.html', {'form':form, 'submitted':submitted})

    



def rent(request) :
    return render(request, 'core/rent.html')

def privacy(request) :
    return render(request, 'core/privacy.html')

def consultation(request):
    return render(request, 'core/consultation.html')