from email import message
from signal import signal
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from services.views import Service
from .models import *
from users.models import profile
from services.models import *

from .forms import messageToForm
# Create your views here.
@login_required(login_url='login')
def MessageSendPage(request):
    id = request.user.profile_set.values()[0]['id']
    profiles =profile.objects.get(pk=id)
    messageRequests = profiles.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    # messageRequests = set(messageRequests.mess_sender)
    # elif request.GET['get'] == "Recieve":
        # messageRequests = profiles.messages.all()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}

    if profiles.role == 'Supplier':
        return render(request,'message.html',context)
    if profiles.role == 'Consumer':
        return render(request,'customer/message.html',context)


@login_required(login_url='login')
def MessageReceivePage(request):
    id = request.user.profile_set.values()[0]['id']
    profiles =profile.objects.get(pk=id)
    messageRequests = profiles.messageto_set.filter(mess_receiver=profiles)

    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    
    if profiles.role == 'Supplier':
        return render(request,'message.html',context)
    if profiles.role == 'Consumer':
        return render(request,'customer/message.html',context)


@login_required(login_url='login')
def createMessage(request,pk):
    id = request.user.profile_set.values()[0]['id']
    profiles =profile.objects.get(pk=id)
    service = Event_Services.objects.get(id=pk)
    receiver = service.service_owner
    messageForm = messageToForm()
    
    if request.method =="POST":
        form = messageToForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.mess_sender = profiles
            message.mess_receiver = receiver
            message.mess_service = service
            message.email = profiles.email
            message.save()
        else:
            print({{form.error}})
    context = {'messageForm':messageForm}
    return render(request,'customer/messageForm.html',context)