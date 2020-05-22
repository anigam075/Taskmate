from django.shortcuts import render,redirect
from .forms import CustomForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        registerform=CustomForm(request.POST)
        if registerform.is_valid():
            registerform.save()
            messages.success(request, ("New user account created"))
            return redirect('register')
    else:
        registerform=CustomForm()
    return render(request, 'register.html', {'registerform':registerform})