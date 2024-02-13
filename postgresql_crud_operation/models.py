from django.db import models

class Employee_details(models.Model):
    emp_id = models.CharField(max_length = 3)
    emp_name = models.CharField(max_length = 50)
    emp_email = models.EmailField()
    emp_gender = models.CharField()
    emp_designation = models.CharField()

    class Meta:
        db_table="Employee_details"

        
