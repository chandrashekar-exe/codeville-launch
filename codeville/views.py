from django.shortcuts import render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import UserDetail

# Create your views here.
def create_user(request):
    return render(request, 'codeville/index.html', {})

def contributors(request):
    return render(request, 'codeville/contrib.html',{})

@csrf_exempt
def add(request):
    print("In add")
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    phone="+91"+phone
    try:
        user = UserDetail(name=name,email=email,phone=phone)
        print(user)
    except Exception as e:
        return(HttpResponse("False"))
    user.save()
    return(HttpResponseRedirect("True"))
