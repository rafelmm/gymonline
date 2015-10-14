from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    company = forms.CharField(label=_("Your Company"), max_length=150)
    name = forms.CharField(label=_("Your Name"), max_length=150)
    phone = forms.CharField(label=_("Your Phone Number"), max_length=20)
    email = forms.EmailField(label=_("Your Email"))
    message = forms.CharField(widget=forms.Textarea, label=_("Your message"), max_length=1000)