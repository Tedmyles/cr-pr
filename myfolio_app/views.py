from django.shortcuts import render, redirect
from myfolio_app.models import Customers

# Create your views here.
def index(request):
    if request.method == 'POST':
        mycontacts = Customers(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        print(mycontacts)

        mycontacts.save()
        return redirect('index')

    return render(request, 'index.html')

def service(request):
    return render(request, 'service-details.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def starter(request):
    return render(request, 'starter-page.html')



