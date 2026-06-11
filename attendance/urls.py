from django.urls import path
from .views import AttendanceListCreateView, AttendanceDetailView

urlpatterns = [
    path('', AttendanceListCreateView.as_view()),
    path('<int:pk>/', AttendanceDetailView.as_view()),
]