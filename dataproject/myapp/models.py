from django.db import models
class Employee(models.Model):
      Employee_id=models.CharField(max_length=8,help_text="Employee ID")
      Employee_name=models.CharField(max_length=100)
      Employee_post=models.CharField(max_length=100)
      Employee_salary=models.IntegerField()
      Employee_age=models.IntegerField()
      Employee_email=models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('Employee_id','Employee_name','Employee_post','Employee_salary','Employee_age','Employee_email')


# Create your models here.
