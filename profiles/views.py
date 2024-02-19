from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForms
from django.views.generic.edit import CreateView
from .models import userprofile
from django.views.generic import ListView
# Create your views here.
def storefile(file):
    with open('temp/image.jpg','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    dest.close()

class createProfileView(View):
    def get(self,request):
        form=ProfileForms()
        return render(request,'profiles/create_profile.html',{
            "form":form
        })

    def post(self,request):
        submitted_form=ProfileForms(request.POST,request.FILES)
        if submitted_form.is_valid():
            # print("The form is validated")
            # print(request.FILES)
            # storefile(request.FILES['user_image'])
            profile=userprofile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect('/profile')
        return render(request,'profiles/create_profile.html',{
            "form":submitted_form
        })

class createprofile(CreateView):
    template_name='profiles/create_profile.html'
    model = userprofile
    fields='__all__'
    success_url='profile/'

class listprofile(ListView):
    model=userprofile
    template_name='profiles/listprofile.html'
    context_object_name='profiles'

 