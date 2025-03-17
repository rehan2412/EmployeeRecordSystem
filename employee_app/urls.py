from django.urls import path
from .views import EmployeeAPI

urlpatterns = [
    path('', EmployeeAPI.as_view(), name='employee_api'),
]
