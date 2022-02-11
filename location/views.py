from django.shortcuts import render
from urllib import response
from django.shortcuts import render,redirect
import urllib.request
from .models import Location
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from route import findpath

# Create your views here.
# Function for saving user input for each checkpoint to database


def home(request):
    if request.method=='POST':
        start_point = request.POST.get('start_point')
        check_point_1 =request.POST.get('check_point_1')
        check_point_2 =request.POST.get('check_point_2')
        check_point_3 =request.POST.get('check_point_3') 
        end_point =request.POST.get('end_point')
        findpath.showroute(start_point,end_point,check_point_1,check_point_2,check_point_3)
        data =Location.objects.create(start_point=start_point,check_point_1=check_point_1,check_point_2=check_point_2,check_point_3=check_point_3,end_point=end_point)
        return HttpResponseRedirect(reverse('result'))
    return render(request,"home.html",{})