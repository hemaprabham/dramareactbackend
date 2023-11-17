from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .serializer import *
from .models import*

# Create your views here.
@csrf_exempt
def viewall(request):
    if request.method=="POST":
        dramalist=Drama.objects.all()
        serialised_data=DramaSerializer(dramalist,many=True)
        return HttpResponse(json.dumps(serialised_data.data))
    
@csrf_exempt    
def addall(request):
    if request.method=="POST":
        receiveddata=json.loads(request.body)
        print(receiveddata)
        serialisercheck=DramaSerializer(data=receiveddata)
        if serialisercheck.is_valid():
            serialisercheck.save()
            return HttpResponse(json.dumps({"status":"success"})) 
        else:
            return HttpResponse(json.dumps({"status":"failed"}))       
@csrf_exempt
def delete(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"student delete"}))      
@csrf_exempt
def search(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"student search"}))          