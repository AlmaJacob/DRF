from django.shortcuts import render
from .models import *
from. serializers import *
from django.http import JsonResponse

# Create your views here.

def sample_fun(req):
    d=Project_user.objects.all()
    s=Sample(d,many=True)
    return JsonResponse(s.data,safe=False)



def modal_fun(req):
    if req.method=='GET':
      d=Project_user.objects.all()
      s=model_serializer(d,many=True)
      return JsonResponse(s.data,safe=False)