from django.contrib import admin
from django.urls import path
from AppSinLuz import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios', views.usuario, name='usuarios'),
    path('post/', views.post, name='post'),
    path('leerUsuarios', views.UsuarioListView.as_view(), name='leerUsuarios'),
    path('leerAdministrativos', views.AdministrativoListView.as_view(), name='leerAdministrativos'),
    path('leerUsuarios/delete/<id_usuario>', views.eliminarUsuario, name='eliminarUsuario'),
    path('leerAdministrativos/delete/<id_administrativo>', views.eliminarAdministrativo, name='eliminarAdministrativo'),
    path('administrativos', views.AdministrativoCreateView.as_view(), name='administrativos'),
    path('leerUsuarios/editar/<pk>', views.UsuarioUpdateView.as_view(), name='editarUsuario'),
    path('leerAdministrativos/editar/<pk>', views.AdministrativoUpdateView.as_view(), name='editarAdministrativos'),
    path('leerUsuarios/eliminar/<pk>', views.UsuarioDeleteView.as_view(), name='eliminarUsuario'),
    path('login', views.login_request, name= 'login'),
    path('register', views.register, name= 'register'),
    path('logout', LogoutView.as_view(template_name='AppSinLuz/logout.html'), name = 'logout'),
    path('about', views.about, name= 'about'),
    path('agregar_avatar', views.agregar_avatar, name='agregar_avatar'),
    path('avatar_success', views.avatar_success, name='avatar_success'),
    path('busquedaReclamo', views.busqueda_reclamo, name='busquedaReclamo'),
    path('buscar/', views.buscar, name='busqueda'),
    path('reclamos', views.reclamos, name='reclamos'),
]