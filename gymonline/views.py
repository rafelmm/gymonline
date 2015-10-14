# -*- coding: utf-8 -*-
from django.shortcuts import render
from datetime import date
from django.utils.timezone import now
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

def home(request):
    today = date.today()
    return render(request, "gymonline/index.html", {'today': today, 'now': now()})

def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def contact(request):
    # Recibimos la respuesta del formulario
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Comprobamos si los datos son validos
        if form.is_valid():
            # Procesamos los datos que tenemos en form.cleaned_data
            subject = 'Contacto de %s' % form.cleaned_data['company']
            message = 'Mensaje de %s:\r\n%s' %(form.cleaned_data['name'],form.cleaned_data['message'])
            sender = form.cleaned_data['email']
            recipients = ['rmormeneo@tugymonline.com']
            send_mail(subject, message, sender, recipients)
            
            # Redirigimos a la nueva url
            messages.success(request, _("Your message has been successfully send. We will contact you as soon as possible. Thanks"))
            return HttpResponseRedirect(reverse('contact'))
    else:
        # Creamos un form vacio
        form = ContactForm()
        
    return render(request, "gymonline/contact.html", {'form': form})

        