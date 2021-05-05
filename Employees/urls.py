from django.conf.urls import url
from .views import createEmployee, success, deleteEmployee, listEmployees, listUnAssigned, idalreadyused

urlpatterns = [

     url('successaddingemployee/', success),
     url('AddEmployee/', createEmployee),
     url('DeleteEmployee/', deleteEmployee),
     url('ListEmployees/', listEmployees),
     url('ListUnAssigned/', listUnAssigned),
     url('idalreadyused/', idalreadyused)
]
