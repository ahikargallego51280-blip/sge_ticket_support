from rest_framework import serializers
from .models import Ticket, Comentario, TicketHistory, Tag, Attachment


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'


class TicketHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketHistory
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    comentarios = ComentarioSerializer(many=True, read_only=True)
    historial = TicketHistorySerializer(many=True, read_only=True)
    adjuntos = AttachmentSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'