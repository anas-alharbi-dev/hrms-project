from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('employees/', include('employees.urls')),
    path('departments/', include('departments.urls')),
    path('attendance/', include('attendance.urls')),
    path('leave/', include('leave.urls')),

    path('dashboard/', include('dashboard.urls')),
    path('reports/', include('reports.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]