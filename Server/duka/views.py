from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Clothes
from .serializer import ClotheSerializer


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to My Duka')


class ClothesList(APIView):
    def get(self, request, format=None):
        all_clothes = Clothes.objects.all()
        serializers = ClotheSerializer(all_clothes, many=True)
        return Response(serializers.data)