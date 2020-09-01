from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def profileview(request):
	form = ProfileForm()

	if request.method=='POST':
		form =ProfileForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return success(request)
	return render(request,'profileapp/display.html',{'form':form})


def success(request):
	s1 = "<center><h1>Profile Upload Sucessfully...</h1></center>"

	return HttpResponse(s1)


def viewProfile(request):
	if request.method=='GET':
		profiles = Profile.objects.all()

		return render(request,'profileapp/image.html',{'profiles':profiles})