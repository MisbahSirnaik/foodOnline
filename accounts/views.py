from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import UserForm
from .models import User

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit = False)
            user.role = User.CUSTOMER
            user.set_password(password)
            user.save()
            messages.success(request, 'Your account has been registered successfully! ')
            return redirect('registerUser')
    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)