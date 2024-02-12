from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=='POST':
        enteredusername=request.POST['username']
        print(enteredusername)
        return HttpResponseRedirect('/ThankYou')
    return render(request,"reviews/index.html")
def Thankspage(request):
    return render(request,"reviews/Thankyou.html")