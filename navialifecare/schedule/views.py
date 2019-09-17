from django.shortcuts import render,redirect
from schedule.models import Userschedule
# Create your views here.

def home(request):
	return render(request,"home.html")


def add(request):
	if request.method=="POST":
		item =  request.POST['medicine']
		time =  request.POST['stime']
		duration = request.POST['duration']
		userref = request.user
		sch = Userschedule(item=item,time=time,duration=duration,userref=userref)
		sch.save()
		data = Userschedule.objects.filter(userref=request.user)
		return render(request,"show.html",{'data':data})
	else:
		data = Userschedule.objects.filter(userref=request.user)		
		return render(request,"add.html",{'data':data})

def show(request):
	data = Userschedule.objects.filter(userref=request.user)
	return render(request,"show.html",{'data':data})