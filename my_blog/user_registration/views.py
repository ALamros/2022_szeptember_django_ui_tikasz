from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    print(request.method)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your account has been created! ")

            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context=context)