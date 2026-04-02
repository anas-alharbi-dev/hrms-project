from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)
   
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employee.objects.filter(user=self.request.user)