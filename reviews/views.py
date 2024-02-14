from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from . import forms
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
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

class singlereviewlist(TemplateView):
    template_name='reviews/singlereview.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        selectedid=kwargs['id']
        reviews=Review.objects.get(id=selectedid)
        context["reviews"]=reviews
        return context
    
class AllReviews(ListView):
    template_name='reviews/reviewslist.html'
    model=Review
    context_object_name="reviews"
    def get_queryset(self):
        base_query=super().get_queryset()
        data=base_query.filter(rating__gt=0)
        return data
class DetailViewsReviews(DetailView):
    template_name='reviews/singlereview.html'
    model=Review

class Formsubmission(FormView):
    form_class=forms.Reviewdb
    template_name='reviews/index.html'
    success_url='/ThankYou'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class Formsubmission1(CreateView):
    model=Review
    form_class=forms.Reviewdb
    template_name='reviews/index.html'
    success_url='/ThankYou'

