from typing import Any
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from . import forms
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
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
class ThankYouView(TemplateView):
    template_name='reviews/Thankyou.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['message']='This Works'
        return context
    
class ReviewList(TemplateView):
    template_name='reviews/reviewslist.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        reviews=Review.objects.all()
        context["reviews"]=reviews
        return context
    