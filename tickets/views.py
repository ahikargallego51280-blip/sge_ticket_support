from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ticket, Comentario
from .serializer import TicketSerializer, ComentarioSerializer


# =========================
# TICKETS
# =========================
@api_view(['GET', 'POST'])
def api_tickets(request):

    # LISTAR
    if request.method == 'GET':
        tickets = Ticket.objects.all().order_by('-fecha_creacion')
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    # CREAR
    if request.method == 'POST':
        serializer = TicketSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# =========================
# EDITAR + BORRAR
# =========================
@api_view(['PUT', 'DELETE'])
def editar_ticket(request, ticket_id):

    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({"error": "No encontrado"}, status=404)

    # EDITAR
    if request.method == 'PUT':
        serializer = TicketSerializer(ticket, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    # BORRAR
    if request.method == 'DELETE':
        ticket.delete()
        return Response({"message": "Eliminado"})


# =========================
# COMENTARIOS
# =========================
@api_view(['POST'])
def crear_comentario(request, ticket_id):

    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response({"error": "Ticket no existe"}, status=404)

    comentario = Comentario.objects.create(
        ticket=ticket,
        autor=request.data.get('autor'),
        texto=request.data.get('texto')
    )

    serializer = ComentarioSerializer(comentario)
    return Response(serializer.data, status=201)