from django.urls import path
from .views import DepartmentListCreateView, DepartmentDetailView

urlpatterns = [
    path('', DepartmentListCreateView.as_view()),
    path('<int:pk>/', DepartmentDetailView.as_view()),
]