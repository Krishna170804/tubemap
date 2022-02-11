"""show_route URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from location.views import home
from route.views import result


admin.site.site_header = 'Krishna Project'
admin.site.site_title = 'Krishna Project'
admin.site.index_title = 'Home'
admin.site.site_url = "https://www.shortest-route.in/"


# URL creation to call out the functions in browser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('result',result,name='result'),
    path('home',home,name='home'),
    ]