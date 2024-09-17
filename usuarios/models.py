

# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('admin', 'Admin'),
        ('employee', 'Empleado'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='employee')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()} - {'Aprobado' if self.is_approved else 'Pendiente'}"
