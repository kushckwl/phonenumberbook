from django import http
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .forms import ContactForm, SignupForm


# Create your views here.
@login_required
def index(request):
    logged_in_user = request.user
    contact = Contact.objects.filter(user=logged_in_user)
    count = User.objects.count()
    context = {'contact':contact, 'count': count}
    
    return render (request, 'phonebook/index.html', context)


def sign(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignupForm()        
    
    context = {'form':form}
    return render (request, 'phonebook/sign.html',context)   

class Create(CreateView):
    model = Contact
    template_name = 'phonebook/create.html'
    form_class = ContactForm
    success_url = '/'
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(Create, self).form_valid(form)
         

class Detail(DetailView):
    model = Contact
    template_name = 'phonebook/detail.html'



class Update(UpdateView):
    model = Contact
    template_name = 'phonebook/update.html'
    form_class = ContactForm
    success_url = '/'    
   
class Delete(DeleteView):
    model = Contact
    template_name = 'phonebook/delete.html'
    success_url = '/'
