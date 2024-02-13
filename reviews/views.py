from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from .models import Review
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.Reviewdb(request.POST)
        if form.is_valid():
            review=Review(user_name=form.cleaned_data['user_name'],review_text=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
            review.save()
            return HttpResponseRedirect("/ThankYou")
    else:   
        form = forms.Reviewdb()
    return render(request,"reviews/index.html",{
        'form':form
    })
def Thankspage(request):
    return render(request,"reviews/Thankyou.html") 