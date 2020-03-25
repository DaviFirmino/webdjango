from django.shortcuts import render
from django.http import HttpResponse
from .models import Work, Contact

def hello_blog (request):
    list_work = Work.objects.all()
    data = {
    'work': list_work }
    return render(request, 'index.html', data)

def work_detail (request, id):
    work = Work.objects.get(id=id)
    return render (request, 'work_detail.html', {'work': work})

def save_form (request):
    name = request.POST['name'],
    Contact.objects.create(
        name = name,
        email = request.POST['email'],
        message = request.POST['message'],
    )
    return render(request, 'contact_ok.html', {'name_contact': name})

# Create your views here.
