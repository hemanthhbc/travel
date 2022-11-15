from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from . models import Place,Team



def demo(request):
   obj = Place.objects.all()
   obj1 = Team.objects.all()
   return render(request,"index.html",{'result':obj,'result1':obj1})



#def addition(request):
  # x=int(request.GET['num1'])
 #  y=int(request.GET['num2'])
 #  add=x+y
 #  sub=x-y
 #  div=x/y
 #  multiplication=x*y
#   return render(request,"result.html",{'result':add,'result1':sub,'result2':multiplication,'result3':div})
