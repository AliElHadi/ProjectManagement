from django.shortcuts import render
from .forms import CreateEmployeeForm, EmployeeDelete
from .models import Employee
from django.http import HttpResponseRedirect


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


def success(request):
    return render(request,'Employees/success.html')


def idalreadyused(request):
    return render(request,'Employees/idalreadyused.html')


def deleteEmployee(request):
    if request.method == 'POST':
        form =EmployeeDelete(request.POST)

        if form.is_valid():
            deleteform = form.cleaned_data
            EID = deleteform['EID']

            for e in Employee.objects.all():
                if e.EID == EID:
                    A = e
                    e.delete()
                    return render(request, 'Employees/sucecessD.html.html')

            return render(request,'Employees/employee_not_found.html', {'form': form})
    else:
        form = EmployeeDelete()
    return render(request, 'Employees/delete_employee.html', {'form': form})


def listEmployees(request):
    return render(request, 'Employees/list_employees.html', {'objects': Employee.objects.all()})


def listUnAssigned(request):
    return render(request, 'Employees/list_unassigned.html', {'objects': Employee.objects.all()})