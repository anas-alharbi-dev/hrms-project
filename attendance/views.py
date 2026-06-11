from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Attendance
from .serializers import AttendanceSerializer


class AttendanceListCreateView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Attendance.objects.all()
        return Attendance.objects.filter(employee__user=self.request.user)


class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Attendance.objects.all()
        return Attendance.objects.filter(employee__user=self.request.user)