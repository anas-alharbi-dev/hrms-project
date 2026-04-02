from django.urls import path
from .views import DepartmentListCreateView

urlpatterns = [
    path('', DepartmentListCreateView.as_view()),

]