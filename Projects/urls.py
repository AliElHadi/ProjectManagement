from django.conf.urls import url
from .views import AddProject, success, home, idfound, listProjectsAssignedwEmployees, \
     deleteProject, listProjectsUnAssigned, match, projects, employees, listE, login, finish, listDone, report, \
     reportProject, reportEmployee, register

urlpatterns = [
#    path('', views.index, name='index'),
     url(r'^$',home),
     url('success/', success),
     url('AddProject/', AddProject),
     url('idfound/',idfound),
     url('lPAwE/', listProjectsAssignedwEmployees),
     url('deleteproject/', deleteProject),
     url('lPUA/', listProjectsUnAssigned),
     url('match/', match),
     url('projects/', projects),
     url('employees/',employees),
     url('listE/',listE),
     url('login/',login),
     url('register/', register),
     url('finish/',finish),
     url('listDone/',listDone),
     url('report/', report),
     url('RP/',reportProject),
     url('RE/', reportEmployee)
]
