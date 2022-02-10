import folium
import requests
from .import getroute

def extractCoordinates(location):
    cordinateString=location.split(",")
    cordinates=[];
    if len(cordinateString)==2: 
        for x in cordinateString:
            print(x)
            cordinates.append(float(x))
    return cordinates

def findOptimumRoute(start,end,checkPoints):
    print(checkPoints)
    routes=[]
    while len(checkPoints)>0: 
        shortest=getroute.get_route(start[1],start[0],checkPoints[0][1],checkPoints[0][0])
        for x in checkPoints:
            route=getroute.get_route(start[1],start[0],x[1],x[0])
            if route['distance']<=shortest['distance']:
                shortest=route
                nextStart=x
        routes.append(shortest)
        start=nextStart
        checkPoints.remove(nextStart)  
        print(routes)
    route=getroute.get_route(start[1],start[0],end[1],end[0])
    routes.append(route)
    return routes

def showroute(startLoc,endLoc,checkPoint1,checkPoint2,checkPoint3):
    start=extractCoordinates(startLoc)
    end=extractCoordinates(endLoc)
    checkPoints=[]
    check1=extractCoordinates(checkPoint1)
    check2=extractCoordinates(checkPoint2)
    check3=extractCoordinates(checkPoint3)
    if len(check1)>0:
        checkPoints.append(check1)
    if len(check2)>0:
        checkPoints.append(check2)
    if len(check3)>0:
        checkPoints.append(check3)
    routeOrder=findOptimumRoute(start,end,checkPoints)
    print(len(routeOrder))
    m = folium.Map(location=[(routeOrder[0]['start_point'][0]),
                                 (routeOrder[0]['start_point'][1])], 
                       zoom_start=10)
    count=0
    startIcon='play'
    stopIcon='stop'
    startColor='green'
    stopColor='red'
    for route in routeOrder:
        count+=1
        if count>1 and count!=len(routeOrder):
            startIcon='stop'
            stopIcon="stop"
            startColor='blue'
            stopColor='blue'        
        elif count==len(routeOrder):
            startIcon='stop'
            stopIcon="stop"
            startColor='blue'
            stopColor='red' 
        folium.PolyLine(route['route'],weight=8,color='blue',opacity=0.6).add_to(m)
        folium.Marker(location=route['start_point'],icon=folium.Icon(icon=startIcon, color=startColor)).add_to(m)
        folium.Marker(location=route['end_point'],icon=folium.Icon(icon=stopIcon, color=stopColor)).add_to(m)
    m.save('./templates/result.html')