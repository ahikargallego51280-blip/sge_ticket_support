from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comentario
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TicketSerializer

def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-fecha_apertura')
    return render(request, 'tickets/ticket_list.html', {
        'tickets': tickets
    })


def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':

        if 'texto' in request.POST:
            Comentario.objects.create(
                ticket=ticket,
                autor=request.POST['autor'],
                texto=request.POST['texto']
            )
            return redirect('ticket_detail', id=ticket.id)

        if 'estado' in request.POST:
            ticket.estado = request.POST['estado']
            ticket.save()
            return redirect('ticket_detail', id=ticket.id)

    comentarios = Comentario.objects.filter(ticket=ticket).order_by('fecha')

    return render(request, 'tickets/ticket_detail.html', {
        'ticket': ticket,
        'comentarios': comentarios
    })

def create_ticket(request):
    if request.method == 'POST':
        Ticket.objects.create(
            titulo=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
            estado='OPEN',
            prioridad=request.POST['prioridad'],
            usuario_reporta=request.POST['usuario_reporta']
        )
        return redirect('ticket_list')

    return render(request, 'tickets/create_ticket.html')

def delete_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return redirect('ticket_list')

@api_view(['GET'])
def api_tickets(request):

    tickets = Ticket.objects.all()

    serializer = TicketSerializer(tickets, many=True)

    return Response(serializer.data)