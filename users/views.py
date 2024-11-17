from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

from .forms import UserRegisterForm

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created successfully!')
            return redirect('users:login')
        else:
            form = UserRegisterForm()
            return render(request=request,
                            template_name='users/register.html',
                            context={
                                'form': form,
                            })
