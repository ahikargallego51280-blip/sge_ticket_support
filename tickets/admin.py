from django.contrib import admin
from .models import Ticket, Usuario, Tecnico

admin.site.register(Ticket)
admin.site.register(Usuario)
admin.site.register(Tecnico)