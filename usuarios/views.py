from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .forms import LoginForm, RegisterForm, CustomPasswordResetForm
from .models import UserProfile, User

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        user = form.get_user()
        if not user.is_active:
            messages.error(self.request, 'Tu cuenta aún no ha sido aprobada por un administrador.')
            return self.form_invalid(form)
        return super().form_valid(form)
@user_passes_test(lambda u: u.is_staff)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Tu cuenta ha sido creada y está pendiente de aprobación por un administrador.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def approve_users(request):
    pending_users = UserProfile.objects.filter(is_approved=False, user__is_active=False)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        action = request.POST.get('action')
        if user_id and action:
            user_profile = UserProfile.objects.get(id=user_id)
            if action == 'approve':
                user_profile.is_approved = True
                user_profile.user.is_active = True
                user_profile.user.save()
                user_profile.save()
                messages.success(request, f'Usuario {user_profile.user.username} aprobado.')
            elif action == 'reject':
                user_profile.user.delete()
                messages.success(request, f'Usuario {user_profile.user.username} rechazado y eliminado.')
        return redirect('approve_users')
    return render(request, 'approve_users.html', {'pending_users': pending_users})

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