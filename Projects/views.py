from django.shortcuts import render, redirect
from .forms import CreateProjectForm, deleteproject, matchform, finishform, RPform, REform, CreateUserForm
from .models import Project
from django.http import HttpResponseRedirect
from Employees.models import Employee
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request,'Projects/home.html')


def AddProject(request):
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            projID = formdata['projID']
            name = formdata['name']
            description = formdata['description']
            status = formdata['status']
            image = formdata['image']
            t = False
            for p in Project.objects.all():
                if projID == p.projID:
                    return HttpResponseRedirect('/idfound')
            for e in Employee.objects.all():
                if e.ProjectID == projID:
                    t = True
            if t:
                status = 'assigned'
            else:
                status = 'unassigned'
            Project.objects.create(projID = projID,name=name,description=description,status=status,image=image)
            return HttpResponseRedirect('/success')
    else:
        form = CreateProjectForm()
    return render(request, 'Projects/createproject.html', {'form': form})


def success(request):
    return render(request, 'Projects/success.html')


def idfound(request):
    return render(request,'Projects/idfound.html')


def listProjectsAssignedwEmployees(request):
    return render(request, 'Projects/listPAwE.html',{'P': Project.objects.all(), 'E': Employee.objects.all()})


def listProjectsUnAssigned(request):
    return render(request, 'Projects/listPUA.html',{'P':Project.objects.all()})


def deleteProject(request):
    if request.method == 'POST':
        form =deleteproject(request.POST)

        if form.is_valid():
            deleteform = form.cleaned_data
            projID = deleteform['projID']

            for p in Project.objects.all():
                if p.projID == projID:
                    p.delete()
                    for e in Employee.objects.all():
                        if e.ProjectID == projID:
                            b = Employee(EID=e.EID,Name=e.Name,ProjectID='0',Expertise=e.Expertise, TotalNumberProjectsDone=e. TotalNumberProjectsDone,Status='unassigned',image=e.image)
                            e.delete()
                            b.save()
                    return render(request, 'Projects/successD.html', {'form': form})
            return render(request,'Projects/project_not_found.html', {'form': form})
    else:
        form = deleteproject()
    return render(request, 'Projects/delete_project.html', {'form': form})


def match(request):
    if request.method == 'POST':
        form =matchform(request.POST)

        if form.is_valid():
            Matchform = form.cleaned_data
            projID = Matchform['projID']
            EID = Matchform['EID']

            for p in Project.objects.all():
                if p.projID == projID:
                    for e in Employee.objects.all():
                        if e.EID == EID and e.Status == 'unassigned':
                            b = Employee(EID=e.EID, Name=e.Name, ProjectID=projID, Expertise=e.Expertise, TotalNumberProjectsDone=e.TotalNumberProjectsDone, Status='assigned',image=e.image)
                            e.delete()
                            b.save()
                            e1= e
                    f = Project(projID=p.projID, name=p.name, description=p.description, status='assigned',image=p.image)
                    p.delete()
                    f.save()
                    return render(request, 'Projects/successA.html')

    else:
        form = matchform()
    return render(request, 'Projects/match.html', {'form': form, 'em': Employee.objects.all(), 'pr': Project.objects.all()})


def projects(request):
    return render(request, 'Projects/projects.html')


def employees(request):
    return render(request, 'Projects/employees.html')


def listE(request):
    return render(request, 'Projects/listE.html')


def listDone(request):
    return render(request, 'Projects/listDone.html', {'P':Project.objects.all()})


def report(request):
    return render(request,'Projects/report.html')


def reportEmployee(request):
    if request.method == 'POST':
        form =REform(request.POST)

        if form.is_valid():
            rEform = form.cleaned_data
            EID = rEform['EID']

            for e in Employee.objects.all():
                if e.EID == EID:
                    return render(request, 'Projects/RE.html', {'form': form, 'E': e, 'P': Project.objects.all()})
            return render(request, 'Employees/employee_not_found.html')
    else:
        form = REform()
    return render(request, 'Projects/RE.html', {'form': form})


def reportProject(request):
    if request.method == 'POST':
        form =RPform(request.POST)

        if form.is_valid():
            rPform = form.cleaned_data
            projID = rPform['projID']

            for p in Project.objects.all():
                if p.projID == projID:
                    return render(request, 'Projects/RP.html', {'form': form, 'P': p, 'E': Employee.objects.all()})
            return render(request, 'Projects/project_not_found.html')
    else:
        form = RPform()
    return render(request, 'Projects/RP.html', {'form': form})


def finish(request):
    if request.method == 'POST':
        form =finishform(request.POST)

        if form.is_valid():
            Finishform = form.cleaned_data
            projID = Finishform['projID']

            for p in Project.objects.all():
                if p.projID == projID:
                    for e in Employee.objects.all():
                        if e.ProjectID == projID:
                            t = int(e.TotalNumberProjectsDone) + 1
                            b = Employee(EID=e.EID, Name=e.Name, ProjectID='0', Expertise=e.Expertise, TotalNumberProjectsDone=str(t), Status='unassigned',image=e.image)
                            e.delete()
                            b.save()
                    f = Project(projID=p.projID, name=p.name, description=p.description, status='finished', image=p.image)
                    p.delete()
                    f.save()
                    return render(request, 'Projects/successF.html')

    else:
        form = finishform()
    return render(request, 'Projects/finish.html', {'form': form, 'em': Employee.objects.all(), 'pr': Project.objects.all()})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('http://localhost:8000/login')

    context = {'form': form}
    return render(request, 'Projects/register.html', context)


def loginn(request):
    if request.method == 'POST':
        request.POST.get
    context = {}
    return render(request, 'Projects/login.html', context)


