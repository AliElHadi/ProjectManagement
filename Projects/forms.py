from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


Status_Choices = [('assigned', 'Assigned'), ('unassigned', 'Unassigned')]


class CreateProjectForm(forms.Form):
    projID = forms.CharField(label='ProjectID')
    name = forms.CharField(label="Project Name")
    description = forms.CharField(label="Project Description")
    status = forms.CharField(label="Project Current Status",widget=forms.Select(choices=Status_Choices))
    image = forms.CharField(label="Image URL")


class deleteproject(forms.Form):
    projID = forms.CharField()


class matchform(forms.Form):
    projID = forms.CharField()
    EID = forms.CharField()


class finishform(forms.Form):
    projID = forms.CharField()


class RPform(forms.Form):
    projID = forms.CharField()


class REform(forms.Form):
    EID = forms.CharField()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']