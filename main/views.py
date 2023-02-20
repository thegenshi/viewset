from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from .serializers import StudentsSerializer
from django.shortcuts import get_list_or_404
# Create your views here.

# class StudentView(viewsets.ViewSet):
class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer
    queryset = Students.objects.all()

    # def list(self, request):
    #     queryset = Students.objects.all()
    #     serializer = StudentsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Students.objects.all()
    #     user = get_list_or_404(queryset, pk=pk)
    #     serializer = StudentsSerializer(user)
    #     return Response(serializer.data)