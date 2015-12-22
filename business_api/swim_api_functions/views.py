from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from swim_api_functions.serializers import BusinessSerializer, BusinessTypeSerializer
from django.template import Context, loader
from models import Business, BusinessType

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def business(request, pk, format = None):
    
    try:
        business_str = Business.objects.get(pk=pk)
    except Business.DoesNotExist:
         return JSONResponse(status=404)
    if request.method == 'PUT':
        serializer = BusinessSerializer(business_str, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        snippets = Business.objects.get(pk=pk)
        serializer = BusinessSerializer(snippets)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        business_str.delete()
        return JSONResponse(status=204)


@csrf_exempt
def businesstype(request, format=None):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BusinessTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.data, status= 400)
        return JSONResponse(serializer.errors, status=400)
    else:
        return JSONResponse([], status=400)

