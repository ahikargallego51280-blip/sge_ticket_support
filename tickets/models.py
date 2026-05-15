from django.db import models


class Usuario(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Tecnico(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Ticket(models.Model):
    ESTADOS = [
        ('no_empezado', 'No empezado'),
        ('en_proceso', 'En proceso'),
        ('completado', 'Completado'),
    ]

    PRIORIDADES = [
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    estado = models.CharField(
        max_length=50,
        choices=ESTADOS,
        default='no_empezado'
    )

    prioridad = models.CharField(
        max_length=50,
        choices=PRIORIDADES,
        default='media'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="comentarios"
    )

    autor = models.CharField(max_length=100)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor}"