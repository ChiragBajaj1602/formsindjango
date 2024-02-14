from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.
def storefile(file):
    with open('temp/image.jpg','wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    dest.close()
class createProfileView(View):
    def get(self,request):
        return render(request,'profiles/create_profile.html')

    def post(self,request):
        storefile(request.FILES['image'])
        return HttpResponseRedirect('/profile')