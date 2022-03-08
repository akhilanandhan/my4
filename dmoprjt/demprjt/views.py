from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import team
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})











    # obj1=team.objects.all()
    # return render(request,"index.html",{'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#
#     return render(request,"result.html",{'addition':x+y,'subtraction':x-y,'multiplication':x*y,'division':x/y})

#
# obj1=team.objects.all()
#     return render(request,"index.html",{'result1':obj1})