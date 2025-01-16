from django.shortcuts import render
from .models import Person
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('pooost')
        print(request.POST)
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(full_name, email, password)

        Person.objects.create(full_name=full_name, bio=email,age=10)
        return HttpResponse('Data has succesfully saved')

    people = Person.objects.all()
    a = 10
    return render(request,"index.html", {'ps': people,'a': a} )