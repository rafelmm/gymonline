# -*- coding: utf-8 -*-
from django.shortcuts import render
#from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .forms import ContactForm

def home(request):
    # Recibimos la respuesta del formulario
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Comprobamos si los datos son validos
        if form.is_valid():
            # Guardamos los datos a la base de datos
            form.save()
            
            # Procesamos los datos que tenemos en form.cleaned_data
            subject = 'Contacto de %s' % form.cleaned_data['company']
            
            message = "Mensaje de %s\r\n"\
                      "Empresa: %s\r\n"\
                      "email: %s\r\n"\
                      "Teléfono: %s\r\n"\
                      "Mensaje:\r\n%s" % ( form.cleaned_data['name'],
                                           form.cleaned_data['company'],
                                           form.cleaned_data['email'],
                                           form.cleaned_data['phone'],
                                           form.cleaned_data['message'])
            sender = form.cleaned_data['email']
            recipients = ['rmormeneo@tugymonline.com','info@tugymonline.com']
            send_mail(subject, message, sender, recipients)
            
            # Redirigimos a la nueva url
            messages.success(request, _("Your message has been successfully send. We will contact you as soon as possible.\nThank you very much"))
            return HttpResponseRedirect(reverse('gymcontact:contact'))
    else:
        # Creamos un form vacio
        form = ContactForm()
        
    return render(request, "gymcontact/contact.html", {'form': form})
