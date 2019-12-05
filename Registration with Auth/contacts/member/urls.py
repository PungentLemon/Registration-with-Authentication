from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path('', views.Home.as_view(), name='home'),
    #members CRUD
    path('contacts', views.ContactList.as_view(), name='contact_list'),
    path('contact/<int:pk>', views.ContactDetail.as_view(), name='contact_detail'),
    path('create', views.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_edit'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
    #auth
    
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]
