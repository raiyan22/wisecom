## Backend Project with Django REST Framework

This project is basically a company management backend web application. It has Company model and Employee model. The relation is one to many (Company -> Employee) and it was implemented through foreign key.
The Company model/class has the following attributes:
```
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=20)
    location= models.CharField(max_length=40)
    about= models.TextField()
    type= models.CharField(max_length=80, choices=(('IT', 'IT'),('Garments', 'Garments'),('Fintech','Fintech')))
    added_date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)
```
The Employee model/class has the following attributes:
```
class Employee(models.Model):
    name= models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    address= models.CharField(max_length=30)
    phone= models.CharField(max_length=10)
    about= models.TextField()
    position= models.CharField(max_length=30,choices=(('project manager','pm'),('team lead','TL'),('software developer', 'sd')))
    company= models.ForeignKey(Company, on_delete=models.CASCADE)
```
The API's that are covered in this project are following:
* http://127.0.0.1:8000/api/v1/companies/
  - GET - Gets a list of all companies
* http://127.0.0.1:8000/api/v1/companies/{companyId}
  - GET - Gets company by Id
* http://127.0.0.1:8000/api/v1/companies/
  - POST - Add a new company
* http://127.0.0.1:8000/api/v1/companies/{companyId}/
  - DELETE - Delete company by Id
* http://127.0.0.1:8000/api/v1/companies/{companyId}/employees/
  - GET - Get the list of employees working under a certain company by companyId
* http://127.0.0.1:8000/api/v1/employees/
  - GET - Gets a list of all employees
* http://127.0.0.1:8000/api/v1/employees/{employeeId}
  - GET - Gets employee by Id
* http://127.0.0.1:8000/api/v1/employees/
  - POST - Add a new employee
* http://127.0.0.1:8000/api/v1/employees/{employeeId}/
  - DELETE - Delete employee by Id

Following are some of the screenshots that were taken during the developmenmt of the project:

Future Work:
The deployment of this project is on going as a part of future work.



