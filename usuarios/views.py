from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Cambia 'home' por la URL a la que quieres redirigir después del registro
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')