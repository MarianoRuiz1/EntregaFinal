from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppSinLuz.forms import AdministrativoForm, AvatarForm, UserRegisterForm, UserLoginForm
from AppSinLuz.models import Administrativo, Avatar, Usuario, Post, Reclamo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/inicio.html', {'avatar_url':avatar_url})

def about(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/about.html', {'avatar_url':avatar_url})

def usuario(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/editarUsuario.html', {'avatar_url':avatar_url})

def post(request):
    posts = Post.objects.filter(estado = True) 
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/post.html', {'posts':posts, 'avatar_url':avatar_url})


def avatarRuscar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/buscar.html', {'avatar_url':avatar_url})

def administrativoForm(request):
    
    if request.method == "POST":
        
        miFormulario_3 = AdministrativoForm(request.POST)
        
        print(miFormulario_3)
        
        if miFormulario_3.is_valid():
            
            informacion_3 = miFormulario_3.cleaned_data
            
            administrativo = Administrativo (usuario=informacion_3['usuario'], contrasena=informacion_3['contrasena'])
            
            administrativo.save()
            
            return render(request, "AppSinLuz/inicio.html")
        
    else:
        
        miFormulario_3 = AdministrativoForm()
        
    return render(request, "AppSinLuz/administrativos.html", {"miFormulario_3":miFormulario_3})


def eliminarUsuario(request, id_usuario):
    
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.delete()
    
    return redirect('usuarios')

def eliminarAdministrativo(request, id_administrativo):
    
    administrativo = Administrativo.objects.get(id=id_administrativo)
    administrativo.delete()
    
    return redirect('administrativo')

class AvatarView:
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['avatar_url'] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        return contexto

class UserDetalle(AvatarView, DetailView):

    model = User
    template_name = "AppSinLuz/leerUsuarios.html"

class UsuarioListView(ListView):
    
    model = Usuario
    template_name = "AppSinLuz/leerUsuarios.html"
    context_object_name = 'usuarios'

    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatares = Avatar.objects.filter(user=self.request.user)
            if avatares:
                contexto['avatar_url'] = avatares.last().imagen.url
        return contexto

   
class AdministrativoListView(ListView):
    
    model = Administrativo
    template_name = "AppSinLuz/leerAdministrativo.html"
    context_object_name = 'administrativos'
    
class UsuarioCreateView(CreateView):
    model = Usuario
    success_url = "register"
    fields = ['username', 'password1', 'password2', 'email', 'direccion', 'departamento']
    template_name = "AppSinLuz/register.html"
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatares = Avatar.objects.filter(user=self.request.user)
            if avatares:
                contexto['avatar_url'] = avatares.last().imagen.url
        return contexto
    
class AdministrativoCreateView(CreateView):
    model = Administrativo
    success_url = "administrativos"
    fields = ['usuario', 'contrasena']
    template_name = "AppSinLuz/administrativos.html"
    
class UsuarioUpdateView(UpdateView):
    
    model = User
    success_url = reverse_lazy('leerUsuarios')
    fields = ['username', 'email', 'last_name', 'first_name']
    template_name = "AppSinLuz/editarUsuario.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            avatares = Avatar.objects.filter(user=self.request.user)
            if avatares:
                contexto['avatar_url'] = avatares.last().imagen.url
        return contexto
   

    
class AdministrativoUpdateView(UpdateView):
    model = Administrativo
    success_url = reverse_lazy('leerAdministrativos')
    fields = ['usuario']
    template_name = "AppSinLuz/administrativos.html"

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('leerUsuarios')
   
class AdministrativoDeleteView(DeleteView):
    model = Administrativo
    success_url = reverse_lazy('leerAdministrativos')

def login_request(request):
    
    if request.method == "POST":
        form = UserLoginForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            
            if user is not None:
                login(request, user)
                
                return render(request, "AppSinLuz/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                
                return render(request, "AppSinLuz/inicio.html", {"mensaje":f"Error, datos incorrectos."})
            
        else:
            
                return render(request, "AppSinLuz/inicio.html", {"mensaje":f"Error, datos incorrectos."})
            
    form = UserLoginForm()
    
    return render(request, "AppSinLuz/login.html", {'form':form})

def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            form.save()
            return render(request, "AppSinLuz/inicio.html", {"mensaje":"Usuario creado"})
        
    else:
        form = UserRegisterForm()
        
    return render(request, "AppSinLuz/register.html", {"form":form})

def agregar_avatar_mostrar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/agregar_avatar.html', {'avatar_url':avatar_url})
    
@login_required
def agregar_avatar(request):

    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            u = User.objects.get(username = request.user)
            avatar = Avatar(user = u, imagen = form.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppSinLuz/avatar_success.html')
    
    form = AvatarForm() 
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/agregar_avatar.html', {'form':form, 'avatar_url':avatar_url})

    
def avatar_success(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/avatar_success.html', {'avatar_url':avatar_url})
    
def buscar(request):
    
    if request.method == "GET":
        fecha = request.GET['fecha']
        reclamos = Reclamo.objects.filter(fecha=fecha)
        return render(request, 'AppSinLuz/buscar.html', {'reclamos':reclamos, 'fecha':fecha})
    else:
        
        respuesta = "No ingreso una fecha."
    return HttpResponse(respuesta)

def busqueda_reclamo(request):
    form = AvatarForm() 
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/busquedaReclamo.html', {'form':form, 'avatar_url':avatar_url})

def reclamos(request):
    
    return render(request, 'AppSinLuz/reclamos.html')

def reclamos(request):
    
    if request.method == "POST":
       fecha = request.POST['fecha']
       detalles = request.POST['detalles']
       print(request.POST)
       Reclamo.objects.create(fecha=fecha, detalles=detalles)
       return render(request, 'AppSinLuz/inicio.html')
    
    form = AvatarForm() 
    avatares = Avatar.objects.filter(user=request.user.id)
    if avatares:
        avatar_url = avatares.last().imagen.url
    else:
        avatar_url = ''
    return render(request, 'AppSinLuz/reclamos.html', {'form':form, 'avatar_url':avatar_url})