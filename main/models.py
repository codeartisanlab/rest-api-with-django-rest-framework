from django.db import models

class Employee(models.Model):
    full_name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=20)
    address=models.TextField()

    def __str__(self):
        return self.full_name
