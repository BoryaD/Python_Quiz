from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
def register(requset):
    if requset.method == 'POST':
        form = UserRegisterForm(requset.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(requset,f'Account created for {username}, You are  now able to log in!')
            return redirect('quize-login')
    else:
        form = UserRegisterForm()

    # form = UserCreationForm()
    return render(requset,'users/register.html',{'title':'Register','form':form})

@login_required
def profile(requset):
    return render(requset, 'users/profile.html')

    # message.debug
    # message.info
    # message.warning
    # message.error