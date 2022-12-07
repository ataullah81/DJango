from django.db import models


# Create your models here.
class Student(models.Model):
    std_id = models.CharField(max_length=100)
    std_name = models.CharField(max_length=200)
    std_email = models.EmailField()
    std_contact_number = models.CharField(max_length=15)
    std_birth_date = models.DateField()

    class Meta:
        db_table = "student"
