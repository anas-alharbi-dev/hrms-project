from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count

from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from leave.models import LeaveRequest


class EmployeeReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            employees = Employee.objects.all()
        else:
            employees = Employee.objects.filter(user=request.user)

        department_distribution = (
            employees
            .values('department__name')
            .annotate(total=Count('id'))
            .order_by('department__name')
        )

        return Response({
            "total_employees": employees.count(),
            "department_distribution": list(department_distribution),
        })


class AttendanceReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            attendance = Attendance.objects.all()
        else:
            attendance = Attendance.objects.filter(employee__user=request.user)

        return Response({
            "total_attendance_records": attendance.count(),
            "completed_attendance": attendance.exclude(check_out=None).count(),
            "open_attendance": attendance.filter(check_out=None).count(),
        })


class LeaveReportView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_staff:
            leaves = LeaveRequest.objects.all()
        else:
            leaves = LeaveRequest.objects.filter(employee__user=request.user)

        return Response({
            "total_leave_requests": leaves.count(),
            "pending_leaves": leaves.filter(status="pending").count(),
            "approved_leaves": leaves.filter(status="approved").count(),
            "rejected_leaves": leaves.filter(status="rejected").count()
        })