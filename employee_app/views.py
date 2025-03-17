from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from dataclasses import dataclass
from functools import wraps
from django.db import IntegrityError, transaction
import time

@dataclass
class EmployeeData:
    employee_id: int
    name: str
    email: str
    department: str
    designation: str
    salary: float
    date_of_joining: str

# Decorators for validation, logging, and execution time
def validate_employee(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            EmployeeData(**data)  # Validate using dataclass
            return func(request, *args, **kwargs)
        except (json.JSONDecodeError, TypeError, ValueError) as e:
            return JsonResponse({"error": "Invalid data", "message": str(e)}, status=400)
    return wrapper

def log_request(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        print(f"Received request: {request.body}")
        return func(request, *args, **kwargs)
    return wrapper

def execution_time(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        start_time = time.time()
        response = func(request, *args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return response
    return wrapper

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeAPI(View):
    @method_decorator(log_request)
    @method_decorator(validate_employee)
    @method_decorator(execution_time)
    def post(self, request):
        data = json.loads(request.body)
        try:
            with transaction.atomic():
                Employee.objects.create(**data)
            return JsonResponse({"message": "Employee added successfully"}, status=201)
        except IntegrityError:
            return JsonResponse({"error": "Duplicate entry or database error"}, status=400)