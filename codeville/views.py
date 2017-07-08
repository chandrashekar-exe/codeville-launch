from django.shortcuts import render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import UserDetail
from django.core.mail import EmailMessage

# Create your views here.
def create_user(request):
    return render(request, 'codeville/index.html', {})

def contributors(request):
    return render(request, 'codeville/contrib.html',{})


# def send_email(recipient):
#     body = '''

#     Hello,

#     Thank you for registering on codeville, to complete your registration, please come to the office on Monday between 10 to 11 am.

#      '''
#     email = EmailMessage('Codeville - Complete your registration', body, to=[recipient])
#     email.send()   

@csrf_exempt
def add(request):
    print("In add")
    name=request.POST['name']
    email=request.POST['email']
    phone=request.POST['phone']
    phone="91"+phone
    # send_email(email)
    try:
        user = UserDetail(name=name,email=email,phone=phone)
    except Exception as e:
        return(HttpResponse("False"))
    user.save()
    return(HttpResponseRedirect("True"))
