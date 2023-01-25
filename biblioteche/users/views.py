from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welocme, {username}")
            return redirect('library-home')
    else:
        form = UserRegistrationForm()
    data = {'form': form}

    return render(request, 'registration.html', data)
