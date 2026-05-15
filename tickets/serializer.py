from rest_framework import serializers
from .models import Ticket, Comentario, Usuario, Tecnico


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'apellidos']


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ['id', 'nombre', 'apellidos', 'especialidad']


class TicketSerializer(serializers.ModelSerializer):

    usuario = UsuarioSerializer(read_only=True)
    tecnico = TecnicoSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id',
            'titulo',
            'descripcion',
            'estado',
            'prioridad',
            'fecha_creacion',
            'usuario',
            'tecnico'
        ]


class ComentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = [
            'id',
            'ticket',
            'autor',
            'texto',
            'fecha'
        ]