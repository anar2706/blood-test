from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):

    form = ContactForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        form.save() 
        
        subject = f'Sizə {request.POST["email"]} dan mesaj var'
        message = 'Ad : ' +request.POST['name']+'\n'+'Məzmun :\n' +request.POST['content']
        email_from = [settings.EMAIL_HOST_USER]
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail( subject, message, email_from, recipient_list )
        messages.success(request,'Istəyiniz uğurla yerinə yetirildi')

        return redirect('contact_f')
    

    

    return render(request,'contact_f.html',context)


