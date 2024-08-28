from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm, UserProfileForm
from .models import UserProfile

User = get_user_model()

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('base')  # o el nombre de tu vista de destino
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            UserProfile.objects.create(user=user, role=role)
            auth_login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido!')
            return redirect('login')  # Cambia 'login' por la URL a la que quieres redirigir después del registro
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def user_edit(request, user_id):
    user = User.objects.get(id=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('user_list')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'user_edit.html', {'form': form, 'user': user})

@login_required
def user_delete(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Usuario eliminado con éxito.')
        return redirect('user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})