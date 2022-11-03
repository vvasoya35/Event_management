from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Service,name='services'),
    path('add-service/',views.Add_Service,name='add-services'),
    path('update-service/<str:pk>',views.Update_Service,name='update-services'),
    path('delete-service/<str:pk>',views.Delete_Service,name='delete-services'),
    path('book-service/<str:pk>',views.Book_Service,name='book-services'),
    path('order-page/',views.Order_Page,name='order-page'),
]