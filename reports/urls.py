from django.urls import path
from .views import EmployeeReportView, AttendanceReportView, LeaveReportView

urlpatterns = [
    path('employees/', EmployeeReportView.as_view()),
    path('attendance/', AttendanceReportView.as_view()),
    path('leaves/', LeaveReportView.as_view()),
]