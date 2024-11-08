# tienda/urls.py
from django.contrib import admin
from django.urls import path, include
from productos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Página de inicio de sesión personalizada
    path('register/', views.register, name='register'),
    path('profile/', views.user_profile, name='user_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),

    # Agregar el namespace 'productos'
    path('productos/', include(('productos.urls', 'productos'), namespace='productos')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
