import uuid
from django.db import models


class Employee(models.Model):
    EID = models.CharField(primary_key=True, max_length=20)
    Name = models.CharField(max_length=20)
    ProjectID = models.CharField(max_length=20)
    Expertise = models.CharField(max_length=30)
    TotalNumberProjectsDone = models.CharField(max_length=3)
    Status = models.CharField(max_length=20, default='Assigned')
    image = models.CharField(max_length=40, default='')

    def __str__(self):
        return "ID: "+ self.EID + " " + self.Name + ": " + self.Expertise + " -> have done " + self.TotalNumberProjectsDone + " projects so far." + "Current Stats: " + self.Status

