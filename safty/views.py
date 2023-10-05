from django.shortcuts import render, HttpResponse, redirect
from safty.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
# from safty.models import Post


def index(request):
    
    return render(request,'index.html')

def act(request):
    return render(request,'acts.html')

def about(request):
    return render(request,'about.html')
 
def rules(request):
    return render(request,'ipcact.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return render(request,'index1.html')
        else:
            return render(request,'index.html')



def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")

def cont(request):
    if request.method == "POST":  
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        
    return render(request, 'contact.html')
 

def logoutUser(request):
    logout(request)
    return render(request,'index.html')

    # the act


def child(request):
    return render(request,'child.html')


def depression(request):
    return render(request,'depression.html')

def rape(request):
    return render(request,'rape.html')



    # sharing the loction
def share(request):
    # from twilio.rest import Client

# sid_="AC369a8c6963ba01b05d6639b70b19680f"
# token_="7482ffd198f6c7817b2a30da7f8be6d7"

# Client=Client(sid_,token_)
# print("yess")
# Client.messages.create(to=["+919307963509"],from_="+18509097667",body="hello this is me tanmay")
# print("message has been send")
# from twilio.rest import Client 
 
# account_sid = 'AC369a8c6963ba01b05d6639b70b19680f' 
# auth_token = '7482ffd198f6c7817b2a30da7f8be6d7' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create(  
#                               messaging_service_sid='MG1c6bf10ffd94354500aaac24cce56652', 
#                               body='hello Tanmay project cha badal discussion karacha ahe ',      
#                               to='+919307963509' 
#                           ) 
 
# print(message.sid)

# Download the helper library from https://www.twilio.com/docs/python/install
    import os
    from twilio.rest import Client

    import json
    from urllib.request import urlopen

    url='http://ipinfo.io/json'
    response=urlopen(url)
    data=json.load(response)
    loc=data['loc']
    ip=data['ip']

# print(data)
# Find your Account SID and Auth Token at twilio.com/console 
# and set the environment variables. See http://twil.io/secure
    account_sid = 'AC369a8c6963ba01b05d6639b70b19680f' 
    auth_token = '7482ffd198f6c7817b2a30da7f8be6d7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body="the location is"+str(loc)+"\n the ip address is"+str(ip),
                              from_='+18509097667',
                              
                              to='+919307963509'
                          )

    print(message.sid)
    return render(request, 'index1.html')


def pc(request):
    return render(request,'pc.html')
def rape1(request):
    return render(request,'rape1.html')
def back(request):
    return render(request,'index.html')
def backlogin(request):
    return render(request,'index1.html')

def rule(request):
    return render(request,'ipcact1.html')
def stalking(request):
    return render(request,'stalking.html')
def sexual(request):
    return render(request,'sexual.html')
def domesticvoilence(request):
    return render(request,'domesticvoilence.html')