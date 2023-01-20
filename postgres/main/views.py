from django.shortcuts import render
from . models import register
from . forms import registrationform

def signup(response):
    if response.method == 'POST':
        form = registrationform(response.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            student_instance = register(name=name, address=address, email=email, phone=phone)

            student_instance.save()
    else:
        form = registrationform()
    return render(response,'main/register.html',{'form':form})
# def signup(response):  
    # data = student.objects.all()
    # return render(response,'main/index.html',{'data':data})
