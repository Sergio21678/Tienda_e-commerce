from django.contrib import admin
from .models import Producto, TipoProducto

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Muestra el nombre en la lista de administración
    search_fields = ('nombre',)  # Permite buscar por nombre

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'tipo_nombre')  # Muestra el nombre, precio y tipo en la lista de administración
    search_fields = ('nombre', 'tipo__nombre')  # Permite buscar por nombre y tipo
    list_filter = ('tipo',)  # Agrega un filtro por tipo en la barra lateral
    ordering = ('nombre',)  # Ordena los productos por nombre de manera ascendente

    def tipo_nombre(self, obj):
        """Devuelve el nombre del tipo de producto."""
        return obj.tipo.nombre if obj.tipo else 'Sin tipo'
    tipo_nombre.short_description = 'Tipo'  # Cambia el encabezado de la columna
