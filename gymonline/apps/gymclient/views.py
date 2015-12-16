# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import get_user_model
from gymonline.apps.gymclient import models
from gymonline.apps.gymclient import forms

@login_required
def home(request):
    return render(request, 
                  "gymclient/home.html",
                  {}
                  )
    
@login_required
def profile_form(request):
    if request.method == "POST":
        profile_form = forms.ProfileForm(request.POST, prefix = "profile")
        user_form = forms.UserForm(request.POST, prefix = "user")
        
        if profile_form.is_valid() and user_form.is_valid():
            user = get_user_model().objects.get(id=request.user.id)
            user.email = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.save()
            
            profile = user.profile
            profile.birthday = profile_form.cleaned_data['birthday']
            profile.gender = profile_form.cleaned_data['gender']
            profile.postal_code = profile_form.cleaned_data['postal_code']
            profile.phone = profile_form.cleaned_data['phone']                 
            profile.nif = profile_form.cleaned_data['nif']
            profile.city = profile_form.cleaned_data['city']
            profile.address = profile_form.cleaned_data['address']
            profile.save()
            
            return HttpResponseRedirect(reverse('gymclient:home'))
    else:
        profile_form = forms.ProfileForm(instance=request.user.profile, prefix="profile")
        user_form = forms.UserForm(instance=request.user, prefix="user")
        return render(request,
                      "gymclient/profile_detail.html",
                      {'profile': profile_form,
                       'user': user_form}
                      )
@login_required 
def class_list(request):
    clase = models.GymClass.objects.all()
    return render(request,
                  "gymclient/clase_list.html",
                  {'claselist': clase}
                  )

@login_required
def class_detail(request, classid):
    classid = int(classid)
    clase = get_object_or_404(models.GymClass, id=classid)
    return render(request,
                  "gymclient/clase_detail.html",
                  {'clase': clase}
                  )

@permission_required(['gymclient.add_gymclass','gymclient.change_gymclass','gymclient.delete_gymclass'], raise_exception=True )
def class_form(request, classid=None):
    if request.method == "POST":
        clase_form = forms.ClassForm(request.POST)
        if clase_form.is_valid():
            clase = clase_form.save()
            return HttpResponseRedirect(reverse('gymclient:home'))
    else:
        if classid:
            clase = get_object_or_404(models.GymClass, id=id)
            clase_form = forms.ClassForm(instance=clase)
        else:
            clase_form = forms.ClassForm()
        return render(request,
                      "gymclient/clase_form.html",
                      {'clase_form': clase_form}
                      )
