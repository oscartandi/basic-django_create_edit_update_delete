from rest_framework.decorators import api_view
from django.forms import ValidationError
from rest_framework.response import Response
from .models import Employee
from .serializer import EmployeeSerializer
from django.shortcuts import render



@api_view(["GET"])
def get_employee(request):
    employee_list=Employee.objects.all()
    serializer = EmployeeSerializer(employee_list, many=True)
    return Response(dict(data=serializer.data))

@api_view(["PATCH"])
def edit_employee(request, emp_id):
    query_parameters = request.query_params
    fullname = query_parameters.get("fullname")
    emp_code = query_parameters.get("emp_code")
    mobile = query_parameters.get("mobile")
    position = query_parameters.get("position")
    edit_employee = Employee.objects.get(id=emp_id)
    print(emp_id)
    edit_employee.update(fullname=fullname, emp_code=emp_code, mobile=mobile, position=position)
    edit_employee.save(update_fields=[fullname, emp_code, mobile, position])
    edited_employee=edit_employee
    return Response(dict(data=edited_employee, id=emp_id))

@api_view(["POST"])
def employee_details(request):  
    fullname = request.data.get("fullname") 
    emp_code = request.data.get("emp_code") 
    mobile = request.data.get("mobile")  
    position = request.data.get("position")  
    Employee.objects.create(  
        fullname = fullname,
        emp_code=emp_code,
        mobile=mobile,
        position=position,
    )  
    return Response(dict(result=True))


@api_view(["DELETE"])
def delete_employee(request, emp_id):
    employee = Employee.objects.get(id=emp_id).delete()
    Employee.save()