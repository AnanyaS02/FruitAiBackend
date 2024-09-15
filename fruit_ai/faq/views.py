from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from .models import FAQ
from .serializers import FAQSerializer
from django.core import serializers
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Utility functions for serialization
def serialize_data(data):
    serializer = FAQSerializer(data, many=True)
    return JSONRenderer().render(serializer.data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def get_faqs(request):
    if request.method == "GET":
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = FAQSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def get_faq(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    if request.method == "GET":
        serializer = FAQSerializer(faq)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = FAQSerializer(faq, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        faq.delete()
        return JsonResponse({'message': 'FAQ deleted'}, status=204)

@csrf_exempt
def add_faq(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FAQSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def update_faq(request, pk):
    faq = FAQ.objects.get(pk=pk)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FAQSerializer(faq, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def delete_faq(request, pk):
    faq = FAQ.objects.get(pk=pk)
    if request.method == 'DELETE':
        faq.delete()
        return JsonResponse({'message': 'FAQ deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
