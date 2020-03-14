from django.shortcuts import render,redirect
from .models import RoomType,Purpose,Location,Room
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from .serializers import RoomTypeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .import models
import json

# Create your views here.

class RoomTypeList(APIView):
    def get(self,request):
        roomtype=RoomType.objects.all()
        serializer=RoomTypeSerializer(roomtype,many=True)
        return Response(serializer.data)
        
def index(request):
    
    AllRoomTypes=RoomType.objects.all()
    return render(request,'index.html',{'rooms':AllRoomTypes})
    
def roomtypes(request):
    return render(request,'roomtypes.html')
    
def RoomTypeCreate(request):
    name=request.POST['name']
    description=request.POST['description']
    
    RoomTypeCreate=RoomType(name=name,description=description)
    RoomTypeCreate.save()
   
    
    return redirect('index')
    
def getAllRooms(request):
    #AllRoomTypes=RoomType.objects.all()
    data=serializers.serialize('json',RoomType.objects.all(),fields=('name','description'))
    
    return HttpResponse(data,content_type="application/json")
    

    
