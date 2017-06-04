from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework import permissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from components.serializers import *
from components.models import *


class OperatingSystemListUI(ListCreateAPIView):

    """
    Showing list of operating systems in UI 
    """

    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@csrf_exempt
def os_list(request):
    """
    List all operating systems or add new system
    """
    if request.method == 'GET':
        os = OperatingSystem.objects.all()
        serializer = OperatingSystemSerializer(os, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OperatingSystemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def os_detail(request, pk):
    """
    Retrieve, update or delete oparating systems.
    """
    try:
        os = OperatingSystem.objects.get(pk=pk)
    except OperatingSystem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OperatingSystemSerializer(os)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OperatingSystemSerializer(os, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        os.delete()
        return HttpResponse(status=204)

class ServerListUI(ListCreateAPIView):

    """
    Showing list of servers in UI
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@csrf_exempt
def server_list(request):
    """
    List all servers or add new server
    """
    if request.method == 'GET':
        server = Server.objects.all()
        serializer = ServerSerializer(server, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ServerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def server_detail(request, pk):
    """
    Retrieve, update or delete servers
    """
    try:
        server = Server.objects.get(pk=pk)
    except OperatingSystem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServerSerializer(server)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServerSerializer(server, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        os.delete()
        return HttpResponse(status=204)

@csrf_exempt
def server_detail_by_name(request, name):
    """
    Retrieve, update or delete servers by their hostname
    """
    try:
        server = Server.objects.get(hostname=name)
    except OperatingSystem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ServerSerializer(server)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ServerSerializer(server, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        os.delete()
        return HttpResponse(status=204)
