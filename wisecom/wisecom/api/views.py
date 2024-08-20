from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class= CompanySerializer

    # companies/{companyID}/'employees' 
    @action(detail=True, methods=['get']) # detail=true mean must pass company id as pk
    def employees(self, request, pk=None): # must be same name as inside ''
        # print("get employees of company " + pk )
        try: 
            company = Company.objects.get(pk=pk) # get the company
            emps = Employee.objects.filter(company=company) # get the emps from that specific comp

            # serialize then pass the json
            emps_serializer=EmployeeSerializer(emps, many=True, context={'request':request})

            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message' : "Company might not be existing"
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer
