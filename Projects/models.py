from django.db import models
from Employees.models import Employee


class Project(models.Model):
    projID = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    image = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name + ":" + self.description + "-->" + self.status
