from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from articles.models import Article

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    cliente = models.CharField(max_length=255)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    def clean(self):
        # Validar que la fecha no sea futura
        if self.fecha and self.fecha > timezone.now().date():
            raise ValidationError({'fecha': "La fecha de venta no puede ser futura."})

        # Validar que el artículo tenga stock suficiente (asumiendo que Article tiene un campo 'stock')
        if self.articulo and self.articulo.stock < 1:
            raise ValidationError({'articulo': "No hay stock suficiente para este artículo."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta {self.id}"
    