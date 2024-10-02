# Ex02 Django ORM Web Application
## Date: 2/10/2024
## Vasanthraj.J

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin
# Register your models here.
admin.site.register(Employee,EmployeeAdmin)

models.py

from django.db import models
from django.contrib import admin
# Create your models here.
class Employee (models.Model):
    eid=models.CharField(max_length=20,help_text="Employee")
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','email')
```

## OUTPUT
![orm](https://github.com/CHANDRUMANIKANDAN/ORM/assets/118644502/ef71bb91-eef5-4533-94dd-4359b5383a97)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
