from rest_framework import viewsets
from .models import Ticket, Comentario
from .serializers import TicketSerializer, ComentarioSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-fecha_apertura')
    serializer_class = TicketSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by('-fecha')
    serializer_class = ComentarioSerializer