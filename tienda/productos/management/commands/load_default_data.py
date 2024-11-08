from django.core.management.base import BaseCommand
from productos.models import TipoProducto

class Command(BaseCommand):
    help = 'Crea tipos de productos predeterminados para la tienda'

    def handle(self, *args, **kwargs):
        tipos = ['Gaseosas', 'Cervezas', 'Licores', 'Cigarros', 'Galletas', 'Agua Mineral', 'Snacks']
        for tipo in tipos:
            TipoProducto.objects.get_or_create(nombre=tipo)
        self.stdout.write(self.style.SUCCESS('Tipos de productos creados exitosamente'))
