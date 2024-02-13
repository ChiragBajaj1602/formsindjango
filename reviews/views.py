from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import forms
from .models import Review
from django.views import View
# Create your views here.
class reviewView(View):
    def get(slef,request):
        form = forms.Reviewdb()
        return render(request,"reviews/index.html",{
            "form":form
        })
    def post(self,request):
        form = forms.Reviewdb(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ThankYou")
        else:   
            form = forms.Reviewdb()
        return render(request,"reviews/index.html",{
        'form':form
    })


def index(request):
    if request.method == 'POST':
        form = forms.Reviewdb(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ThankYou")
    else:   
        form = forms.Reviewdb()
    return render(request,"reviews/index.html",{
        'form':form
    })
def Thankspage(request):
    return render(request,"reviews/Thankyou.html")