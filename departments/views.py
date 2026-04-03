from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated


class DepartmentListCreateView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


        # TODO" improve permissions