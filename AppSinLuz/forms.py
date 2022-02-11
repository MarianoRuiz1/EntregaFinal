from django import forms
from django.forms import CharField, EmailField, PasswordInput, Form, ImageField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    
    username = CharField(label='Usuario', help_text = False)
    password1 = CharField(label='Contraseña', widget = PasswordInput, help_text = False)
    password2 = CharField(label='Confirmar contraseña', widget = PasswordInput, help_text = False)
    email = EmailField(label='Email', help_text = False)
    direccion = CharField(help_text = False)
    piso_dpto = CharField(help_text = False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'direccion', 'piso_dpto']
        help_texts = {k:"" for k in fields}
    
class AdministrativoForm(forms.Form):
    usuario = forms.CharField(max_length=50)
    contrasena = forms.CharField(max_length=50)
    
class UserRegisterForm(UserCreationForm):
    
    username = CharField(label='Usuario', help_text = False)
    password1 = CharField(label='Contraseña', widget = PasswordInput, help_text = False)
    password2 = CharField(label='Confirmar contraseña', widget = PasswordInput, help_text = False)
    email = EmailField(label='Email', help_text = False)
    last_name = CharField(label='Apellido', help_text = False)
    first_name = CharField(label='Nombre', help_text = False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k: "" for k in fields}

class UserLoginForm(AuthenticationForm):
    
    username = CharField(label='Usuario', help_text = False)
    password = CharField(label='Contraseña', widget = PasswordInput, help_text = False)
    
    
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {k: "" for k in fields}

class AvatarForm(Form):
    imagen = ImageField(required=True)

class ReclamoForm(forms.Form):
    
    problema = forms.CharField(max_length=30)
    fecha = forms.DateField()
    resumen = forms.CharField(max_length=50)
    detalles = forms.CharField(max_length=200)
