from django.db import models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=20)
    location= models.CharField(max_length=40)
    about= models.TextField()
    type= models.CharField(max_length=80, choices=(('IT', 'IT'),('Garments', 'Garments'),('Fintech','Fintech')))
    added_date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)

    def __str__(self):
        return self.name + " - " + self.location

class Employee(models.Model):
    name= models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    address= models.CharField(max_length=30)
    phone= models.CharField(max_length=10)
    about= models.TextField()
    position= models.CharField(max_length=30,choices=(('project manager','pm'),('team lead','TL'),('software developer', 'sd')))
    company= models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name