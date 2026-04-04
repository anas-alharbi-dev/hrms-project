from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer


class LeaveListCreateView(generics.ListCreateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(employee__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user.employee)


class LeaveDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return LeaveRequest.objects.all()
        return LeaveRequest.objects.filter(employee__user=self.request.user) 