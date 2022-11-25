from django.urls import path, include
from .views import Employee
from . import views


urlpatterns = [
    path('get/', views.get_employee, name="employee_list"),
    path('create/', views.employee_details, name='create_employee'),
    path('<int:emp_id>/update/', views.edit_employee, name='update_employee'),
    path('<int:emp_id>/delete/', views.delete_employee, name='delete_employee')

]


#path('post/', views.edit_employee, name='edit_employee'),