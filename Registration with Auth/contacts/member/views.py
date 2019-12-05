from django.views.generic import (ListView, DetailView, CreateView,
                                    UpdateView, DeleteView, TemplateView)
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

def index(request):
    return render(request,'member/index.html')

class ContactList(ListView):
    model = Contact

class ContactDetail(DetailView):
    model = Contact


class ContactCreate(CreateView):
    model = Contact
    fields= ['name','email','address','phone']
    def contact_detail(self,request):
        if request.method=="POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()

    def get_success_url(self):
         return reverse_lazy('contact_list')



class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name','email','address','phone']
    template_name_suffix = '_update_form'
    def contact_detail(self,request):
        if request.method=="POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()

    def get_success_url(self):
         return reverse_lazy('contact_list')

class ContactDelete(DeleteView):
    model = Contact

    def get_success_url(self):
         return reverse_lazy('contact_list')

#Authentication

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'member/signup.html'

class Home(TemplateView):
    template_name= 'member/home.html'

class PasswordReset(TemplateView):
    template_name= 'password_reset_form.html'