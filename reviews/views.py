from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/ThankYou")
    else:   
        form = forms.ReviewForm()
    return render(request,"reviews/index.html",{
        'form':form
    })
def Thankspage(request):
    return render(request,"reviews/Thankyou.html") 