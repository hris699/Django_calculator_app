from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from calc.models import Calculation, Memory
from calc.serializers import  MemorySerializer

# Create your views here.

@csrf_exempt
def Calc(request):
    print(request)
    try:
        data=JSONParser().parse(request)
        print(data)
        data=data["client"]
        while data[-1]  in ["+","-","*","/"]:
            data=data[0:-1]
        while data[0]  in ["+","*","/"]:
            data=data[1:]
        res=eval(data)
        calculation=Calculation(operation=data,result=res)
        calculation.save()
    except:
        res="Not Defined"
    return JsonResponse(str(res),safe=False)

@csrf_exempt
def mcOperation(request):
    data=Memory.objects.all()
    data.delete()
    mc=Memory(number="")
    mc.save()
    print("request for object delete")
    return JsonResponse("memory cleared",safe=False)

@csrf_exempt
def msOperation(request):
    try:
        data=JSONParser().parse(request)
        data=data["client"]
        res=eval(data)
        ms=Memory.objects.all()
        ms.delete()
        mc=Memory(number=res)
        mc.save()
    except:
        res="Not Defined"
    return JsonResponse(str(res),safe=False)

@csrf_exempt
def mrOperation(request):
    res=Memory.objects.all()
    serialise=MemorySerializer(res,many=True)
    res=serialise.data[0]["number"]
    return JsonResponse(res,safe=False)

@csrf_exempt
def mAddOperation(request):
    try:
        data=JSONParser().parse(request)
        data=data["client"]
        res=eval(data)
        print("res",res)
        madd=Memory.objects.all()
        serialise=MemorySerializer(madd,many=True)
        memoRes=serialise.data[0]["number"]  # gives back an ordered dictonary
        madd.delete()
        print("memoRes",memoRes)
        if memoRes=="":
            memory=Memory(number=int(res)+int(0))
            memory.save()
        else:
            memory=Memory(number=int(res)+int(memoRes))
            memory.save()
    except:
        madd=Memory.objects.all()
        serialise=MemorySerializer(madd,many=True)
        memoRes=serialise.data[0]["number"]
        madd.delete()
        if memoRes!="":
            memory=Memory(number=int(memoRes)+int(memoRes))
            memory.save()
        else:
            pass
    madd=Memory.objects.all()
    serialise=MemorySerializer(madd,many=True)
    memoRes=serialise.data[0]["number"]
    return JsonResponse(str(memoRes),safe=False)