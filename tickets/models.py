from django.db import models
from django.contrib.auth.models import User
from users.models import Technician


class Ticket(models.Model):

    ESTADO = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In progress'),
        ('CLOSED', 'Closed'),
    ]

    PRIORIDAD = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    fecha_apertura = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)

    estado = models.CharField(max_length=20, choices=ESTADO, default='OPEN')
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD, default='MEDIUM')

    usuario_reporta = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tickets_reportados"
    )

    tecnico_asignado = models.ForeignKey(
        Technician,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tickets_asignados"
    )

    def __str__(self):
        return self.titulo


class Comentario(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )

    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )

    def __str__(self):
        return f"Comentario en {self.ticket.titulo}"


class TicketHistory(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="historial"
    )

    estado_anterior = models.CharField(max_length=20)
    estado_nuevo = models.CharField(max_length=20)

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket.titulo}: {self.estado_anterior} → {self.estado_nuevo}"


class Tag(models.Model):

    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Attachment(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="adjuntos"
    )

    archivo = models.FileField(upload_to='tickets/')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.archivo.name