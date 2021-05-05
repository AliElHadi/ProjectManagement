from django import forms

ListOfExpertise = [
    ('software developer', 'Software Developer'),
    ('object oriented designer','Object Oriented Designer'),
    ('software tester and debugger','Software Tester and Debugger'),
    ('project manager','Project Manager')
]

ListStatus = [
    ('unassigned', 'UnAssigned'),
    ('assigned', 'Assigned')
]


class CreateEmployeeForm(forms.Form):
    EID = forms.CharField(label='EID')
    Name = forms.CharField(label='name')
    ProjectID = forms.CharField(label='ProjectID')
    Expertise = forms.CharField(label='Expertise', widget=forms.Select(choices=ListOfExpertise))
    TotalNumberProjectsDone = forms.CharField(label='TotalNumberProjectDone')
    Status = forms.CharField(label='Status', widget=forms.Select(choices=ListStatus))
    image = forms.CharField(label='Image URL')


class EmployeeDelete(forms.Form):
    EID = forms.CharField()




