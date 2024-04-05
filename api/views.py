from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter

class TaskListCreateAPIView(generics.ListCreateAPIView):
    
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["status"]  # specify fields for search
    ordering_fields = ['created_at', 'updated_at']
   

    def get_queryset(self):
        # Retrieve tasks associated with the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the user of the task to the currently logged-in user
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retrieve tasks associated with the logged-in user
        return Task.objects.filter(user=self.request.user)
