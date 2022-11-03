from distutils.log import error
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from users.models import *
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt # import

@login_required(login_url='login')
def Service(request):
    try:
        pk = request.user.profile_set.values()[0]['id']
    except:
        pk = request.user.profile
    profiles = profile.objects.get(pk=pk)
    services = profiles.event_services_set.all()
    context = {'services':services,'profile':profiles}
    return render(request,'services/services.html',context)

@login_required(login_url='login')
def Add_Service(request):
    id = request.user.profile_set.values()[0]['id']
    profiles = profile.objects.get(pk=id)
    form = ServicesForm()
    if request.method == 'POST':
        # form = Event_Services.objects.create(service_owner=profiles,service_name=request.POST['service_name'],service_description=request.POST['service_description'],category=request.POST['category'],featured_image=request.POST['featured_image'],price=request.POST['price'])
        form = ServicesForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.service_owner = profiles
            service.save()
            print(service.service_owner)
            
            return redirect('services')
        else:
            print(form.errors)
    context = {'form':form,'profile':profiles}
    return render(request,'services/service-form.html',context)

@login_required(login_url='login')
def Update_Service(request,pk):
    service = Event_Services.objects.get(id=pk)
    id = request.user.profile_set.values()[0]['id']
    profiles =profile.objects.get(pk=id)
    form = ServicesForm(instance=service)
    if service.service_owner.id == id:
        if request.method == 'POST':
            form = ServicesForm(request.POST,request.FILES,instance=service)
            if form.is_valid():
                form.save()
                return redirect('services')
        context = {'form':form,'profile':profiles}
        return render(request,'services/service-form.html',context)
    else:
        return redirect('service-page',pk=service.id)
    

@login_required(login_url='login')
def Delete_Service(request,pk):
    id = request.user.profile_set.values()[0]['id']
    profiles =profile.objects.get(pk=id)
    service = Event_Services.objects.get(id=pk)
    if request.method == 'POST':
        print(service)
        service.delete()
        return redirect('services')
    else:
        context = {'object':service,'profile':profiles}
        return render(request,'delete-form.html',context)
    
@login_required(login_url='login')
def Book_Service(request,pk):
    id = request.user.profile_set.values()[0]['id']
    profiles =profile.objects.get(pk=id)
    service = Event_Services.objects.get(id=pk)
    serviceBookForm = ServiceBookForm()
    if request.method == 'POST':
        address = request.POST['address']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        try:
            form = booking.objects.create(customer=profiles,services=service,address=address,start_date=start_date,end_date=end_date,start_time=start_time,end_time=end_time)
            messages.success(request,'Order Done')
            return redirect('index')
        except:
       
            messages.warning(request,'Invalid Data')
            
    context={'profile':profiles,'serviceBookForm':serviceBookForm}
    return render(request,'customer/bookingForm.html',context)

@login_required(login_url='login')
def Order_Page(request):
    id = request.user.profile_set.values()[0]['id']
    profiles = profile.objects.get(pk=id)
    orders = booking.objects.filter(customer=profiles.id)
    
    # print(profiles)
    print(orders)
    context = {'order':orders,'profile':profiles}
    return render(request,'customer/order.html',context)
