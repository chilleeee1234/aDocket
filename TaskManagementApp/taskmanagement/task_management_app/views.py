from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializers
from .models import task
from django.shortcuts import  render, redirect




class taskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializers
    queryset = task.objects.all()

