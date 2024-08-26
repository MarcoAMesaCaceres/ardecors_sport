# views.py
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm
from django.contrib.auth.decorators import user_passes_test

def is_admin_or_employee(user):
    return user.role in ['admin', 'employee']

@user_passes_test(is_admin_or_employee, login_url='login')
def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and is_admin_or_employee(user):
                auth_login(request, user)
                return redirect('base')  # o el nombre de tu vista de destino
            else:
                messages.error(request, 'Acceso denegado o credenciales incorrectas.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        if is_admin_or_employee(user):
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Acceso denegado.')
            return self.form_invalid(form)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if is_admin_or_employee(user):
                auth_login(request, user)
                return redirect('login')
            else:
                messages.error(request, 'Registro exitoso, pero no tienes permisos para iniciar sesión.')
                return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')