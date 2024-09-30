from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado!!')
            return redirect('contact:user_login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
        },
    )

def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Logado com sucesso')
            auth.login(request,user)
            return redirect('contact:index')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
        },
    )

@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contact:user_login')

@login_required(login_url='contact:login')
def update_view(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Mudanças feitas com sucesso')
            return redirect('contact:index')

    return render(
        request,
        'contact/update_register.html',
        {
            'form': form,
        },
    )
