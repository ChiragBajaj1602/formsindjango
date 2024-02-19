from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForms
from .models import userprofile
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
        else:
            print("The form is invalidated")
        return render(request,'profiles/create_profile.html',{
            "form":submitted_form
        })
    