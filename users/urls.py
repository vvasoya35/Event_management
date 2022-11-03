from django.urls import path, include
from . import views
urlpatterns = [
    
    path('', views.HomePage, name='index'),
    path('service-Detail/<str:pk>', views.ServicePage, name='service-page'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('Register-Supplier/', views.RegisterSupplier, name='Register'),
    path('my-account',views.userAccount,name='my-account'),
    path('my-order/',views.GetOrders,name='my-order'),
    path('accept-order/<str:pk>',views.Accept_Order,name='accept-order'),
    path('complete-order/<str:pk>',views.Complete_Order,name='complete-order'),
]