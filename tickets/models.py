from django.db import models


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

    usuario_reporta = models.CharField(max_length=100)
    tecnico_asignado = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="comentarios")

    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()

    autor = models.CharField(max_length=100)

    def __str__(self):
        return f"Comentario en {self.ticket.titulo}"