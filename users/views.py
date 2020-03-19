from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, You are  now able to log in!')
            return redirect('users-login')
    else:
        form = UserRegisterForm()

    # form = UserCreationForm()
    return render(request, 'users/register.html', {'title': 'Register', 'form': form})


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('users-login')


    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user

        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)


@login_required
def profile(request, user_id):
    print(user_id)
    print(request.user.id)
    if int(user_id) == request.user.id:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                       request.FILES,
                                       instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('users-profile', user_id)

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'coins': Profile.objects.get(user_id=user_id).token,
            'u_form': u_form,
            'p_form': p_form,
            'is_this_user': True
        }

    else:
        user = get_object_or_404(User, id=user_id)
        profile_ = Profile.objects.get(user_id=user.id)
        context = {
            'profile': profile_,
            'is_this_user': False
        }

    return render(request, 'users/profile.html', context)
