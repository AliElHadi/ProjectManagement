from django.shortcuts import render
from .forms import CreateEmployeeForm, EmployeeDelete
from .models import Employee
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Projects.models import Project

@login_required(login_url='http://localhost:8000/login')
def createEmployee(request):
    if request.method == 'POST':
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            EID = formdata['EID']
            Name = formdata['Name']
            ProjectID = formdata ['ProjectID']
            Expertise = formdata['Expertise']
            TotalNumberProjectsDone = formdata['TotalNumberProjectsDone']
            Status = formdata['Status']
            image = formdata['image']
            for e in Employee.objects.all():
                if EID == e.EID:
                    return HttpResponseRedirect('/idalreadyused')
            Employee.objects.create(EID=EID,Name=Name,ProjectID=ProjectID,Expertise=Expertise,TotalNumberProjectsDone=TotalNumberProjectsDone,Status=Status,image=image)
            return HttpResponseRedirect('/successaddingemployee')
    else:
        form = CreateEmployeeForm()
    return render(request, 'Employees/createemployee.html', {'form': form})


@login_required(login_url='http://localhost:8000/login')
def success(request):
    return render(request,'Employees/success.html')


@login_required(login_url='http://localhost:8000/login')
def idalreadyused(request):
    return render(request,'Employees/idalreadyused.html')


@login_required(login_url='http://localhost:8000/login')
def deleteEmployee(request):
    if request.method == 'POST':
        form =EmployeeDelete(request.POST)

        if form.is_valid():
            deleteform = form.cleaned_data
            EID = deleteform['EID']

            for e in Employee.objects.all():
                if e.EID == EID:
                    b = False
                    A = e
                    e.delete()
                    for r in Employee.objects.all():
                        if r.ProjectID == A.ProjectID:
                            b =True
                    if b == False:
                        for p in Project.objects.all():
                            if p.projID == A.ProjectID:
                                f = Project(projID=p.projID, name=p.name, description=p.description, status='unassigned', image=p.image)
                                p.delete()
                                f.save()
                    return render(request, 'Employees/sucecessD.html')

            return render(request,'Employees/employee_not_found.html', {'form': form})
    else:
        form = EmployeeDelete()
    return render(request, 'Employees/delete_employee.html', {'form': form})


@login_required(login_url='http://localhost:8000/login')
def listEmployees(request):
    return render(request, 'Employees/list_employees.html', {'objects': Employee.objects.all()})


@login_required(login_url='http://localhost:8000/login')
def listUnAssigned(request):
    return render(request, 'Employees/list_unassigned.html', {'objects': Employee.objects.all()})