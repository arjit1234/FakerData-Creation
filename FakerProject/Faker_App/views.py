from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
import faker
fake=faker.Faker()

def create_view(request):
    for i in range(1,100+1):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email=fake.email()
        salary=fake.random_element(elements=(10000,15000,20000,56000))
        job=fake.random_element(elements=('IT','Sales','Marketing'))
        location=fake.random_element(elements=('Pune','Hyderbad','Banglore','BBSR'))

        data=Employee(
            first_name=first_name,
            last_name=last_name,
            email=email,
            salary=salary,
            job=job,
            location=location
            )
        data.save()
        return redirect('/')

def fetch_view(request):
    employees=Employee.objects.all()
    return render(request,'Faker_App/index.html',{'employees':employees})

