from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from leave.models import LeaveRequest


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now().date()

        if request.user.is_staff:
            employees = Employee.objects.all()
            departments = Department.objects.all()
            attendance = Attendance.objects.all()
            leave_requests = LeaveRequest.objects.all()
        else:
            employees = Employee.objects.filter(user=request.user)
            departments = Department.objects.filter(user=request.user)
            attendance = Attendance.objects.filter(employee__user=request.user)
            leave_requests = LeaveRequest.objects.filter(employee__user=request.user)

        return Response({
            "total_employees": employees.count(),
            "total_departments": departments.count(),
            "today_attendance": attendance.filter(date=today).count(),
            "pending_leaves": leave_requests.filter(status="pending").count(),
            "approved_leaves": leave_requests.filter(status="approved").count(),
            "rejected_leaves": leave_requests.filter(status="rejected").count(),
            "total_leave_requests": leave_requests.count(),
        })