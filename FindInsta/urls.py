
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from Findfaces.api import viewsets as FindfacesViewsets

route = routers.DefaultRouter()
route.register(r'findface', FindfacesViewsets.FindfacesViewset, basename ="Findfaces")
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)) 
]
