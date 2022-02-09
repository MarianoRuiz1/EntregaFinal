from django.contrib import admin
from AppSinLuz.models import Usuario, Administrativo, Avatar, Post

admin.site.site_header = 'Sin Luz Admin'
admin.site.register(Usuario)
admin.site.register(Administrativo)
admin.site.register(Avatar)
admin.site.register(Post)
admin.site.site_title = "Sin Luz"
admin.site.site_url = "/SinLuz"