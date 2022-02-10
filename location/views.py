from django.shortcuts import render
from urllib import response
from django.shortcuts import render,redirect
import urllib.request
from .models import Location
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from route import findpath

# Create your views here.

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

# def showroute(request,lat1,long1,lat2,long2):
#     figure = folium.Figure()
#     lat1,long1,lat2,long2=float(lat1),float(long1),float(lat2),float(long2)
#     route=getroute.get_route(long1,lat1,long2,lat2)
#     m = folium.Map(location=[(route['start_point'][0]),
#                                  (route['start_point'][1])], 
#                        zoom_start=10)
#     m.add_to(figure)
#     folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
#     folium.Marker(location=route['start_point'],icon=folium.Icon(icon='play', color='green')).add_to(m)
#     folium.Marker(location=route['end_point'],icon=folium.Icon(icon='stop', color='red')).add_to(m)
#     figure.render()
#     context={'map':figure}
#     return render(request,'showroute.html',context)