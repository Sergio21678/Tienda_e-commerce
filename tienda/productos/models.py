from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    tipo = models.ForeignKey('TipoProducto', on_delete=models.CASCADE, related_name='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)  # Usa el nombre como cadena
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.producto.nombre}"

    def get_total_price(self):
        return self.quantity * self.producto.precio
    
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="carrito")
    # Otros campos relacionados con el carrito (productos, cantidades, etc.)