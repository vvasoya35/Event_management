from xmlrpc.client import boolean
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomerForm, ServiceProviderForm
from django.views.decorators.csrf import csrf_exempt # import
from .models import profile
from services.models import Event_Services,Service_Category,Review,booking
# Create your views here.


def HomePage(request):
    # id = request.user.profile_set.all().values()
    # print(id)
    profiles = profile.objects.all()
    service = Event_Services.objects.all()
    context={'profile':profiles,'service':service}
    return render(request,'customer/index.html',context)

@login_required(login_url='login')
def ServicePage(request,pk):
    
    try:
        id = request.user.profile_set.values()[0]['id']
        profiles = profile.objects.get(id=id)
        service = Event_Services.objects.get(id=pk)
        owner = boolean(service.service_owner==profiles)
        # print(owner)
        context={'service':service,'review':review,'count_rivew':count_rivew,'profile':profiles,'owner':owner}
    except:
        owner = boolean(service.service_owner==profiles)
        print(owner)
        service = Event_Services.objects.get(id=pk)
        review = service.review_set.all()
        count_rivew = print(len(review))
        context={'service':service,'review':review,'count_rivew':count_rivew,'owner':owner}
        
    return render(request,'customer/product-page.html',context)



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method=='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User dose not exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # return redirect('services')
            
            return redirect(request.GET['next'] if 'next' in request.GET else 'services')
        else:
            messages.error(request,'Username or password is incorrect')
            return render(request,'login.html')
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def RegisterSupplier(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            form2 = profile.objects.create(owner=user,first_name=request.POST['first_name'],email=request.POST['email'])
            form2.save()
            
            return redirect('login')
    print(form)   
    context={'form':form,'page':page}    
    return render(request,'register.html',context)



@login_required(login_url='login')
def userAccount(request):
    profiles = request.user.profile_set.values()[0]['id']
    pro = profile.objects.get(id =profiles)
    # services = profiles.event_services_set.all()
    form = ServiceProviderForm(instance=pro)
    if request.method == "POST":
        form = ServiceProviderForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
    
    
    context={'profile':pro,
             'form':form,
             }
    return render(request,'user/my-account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = CustomerForm(instance=profile)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html',context)


@login_required(login_url='login')
def GetOrders(request):
    profiles = request.user.profile_set.values()[0]['id']
    service = Event_Services.objects.filter(service_owner=profiles)
   
    orders = booking.objects.filter(services__service_owner=profiles)
    print(orders)
    context={'profile':profiles,'order':orders}
    return render(request,'order.html',context)


@login_required(login_url='login')
def Accept_Order(request,pk):
    book = booking.objects.get(pk=pk)
    book.status='Accept'
    book.save()
    return redirect('my-order')

@login_required(login_url='login')
def Complete_Order(request,pk):
    book = booking.objects.get(pk=pk)
    book.status='Completed'
    book.save()
    return redirect('my-order')
