from django.db import models

class Cliente(models.Model):
    # 1. Campo para el nombre del cliente (CharField)
    nombre = models.CharField(max_length=100, help_text="Nombre completo del cliente")

    # 2. Campo para la dirección de correo electrónico (EmailField)
    email = models.EmailField(unique=True, help_text="Dirección de correo electrónico única del cliente")

    # 3. Campo para el número de teléfono (CharField)
    telefono = models.CharField(max_length=20, blank=True, null=True, help_text="Número de teléfono del cliente (opcional)")

    # 4. Campo para la dirección completa (TextField)
    direccion = models.TextField(blank=True, null=True, help_text="Dirección completa del cliente (opcional)")

    # 5. Campo para la edad (PositiveSmallIntegerField)
    edad = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Edad del cliente (opcional)")


    def __str__(self):
        return f"{self.nombre} {self.email} {self.edad} {self.direccion} {self.telefono}"