<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'

/* =========================
   TICKETS
========================= */
const tickets = ref<any[]>([])
const loading = ref(true)

const modo = ref<'crear' | 'editar'>('crear')

const nuevo = ref<any>({
  id: null,
  titulo: '',
  descripcion: '',
  estado: 'no_empezado',
  prioridad: 'media'
})

const filtroEstado = ref('todos')
const filtroPrioridad = ref('todos')

/* =========================
   COMENTARIOS
========================= */
const ticketActivo = ref<any | null>(null)
const comentarios = ref<any[]>([])

const nuevoComentario = ref({
  autor: '',
  texto: ''
})

const errorComentario = ref('')

/* =========================
   CARGA TICKETS
========================= */
const cargarTickets = async () => {
  const res = await fetch('http://127.0.0.1:8000/api/tickets/')
  tickets.value = await res.json()
  loading.value = false
}

onMounted(cargarTickets)

/* =========================
   FILTROS
========================= */
const ticketsFiltrados = computed(() => {
  return tickets.value
    .filter(t =>
      filtroEstado.value === 'todos' || t.estado === filtroEstado.value
    )
    .filter(t =>
      filtroPrioridad.value === 'todos' || t.prioridad === filtroPrioridad.value
    )
})

/* =========================
   CRUD TICKETS
========================= */
const guardarTicket = async () => {
  if (modo.value === 'crear') {
    await fetch('http://127.0.0.1:8000/api/tickets/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(nuevo.value)
    })

    await cargarTickets()
  } else {
    const res = await fetch(
      `http://127.0.0.1:8000/api/tickets/${nuevo.value.id}/`,
      {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nuevo.value)
      }
    )

    const data = await res.json()

    tickets.value = tickets.value.map(t =>
      t.id === data.id ? data : t
    )
  }

  resetForm()
}

const editar = (t: any) => {
  nuevo.value = { ...t }
  modo.value = 'editar'
}

const eliminar = async (id: number) => {
  await fetch(`http://127.0.0.1:8000/api/tickets/${id}/`, {
    method: 'DELETE'
  })

  tickets.value = tickets.value.filter(t => t.id !== id)

  if (ticketActivo.value?.id === id) {
    ticketActivo.value = null
    comentarios.value = []
  }
}

const resetForm = () => {
  nuevo.value = {
    id: null,
    titulo: '',
    descripcion: '',
    estado: 'no_empezado',
    prioridad: 'media'
  }
  modo.value = 'crear'
}

/* =========================
   DETALLE TICKET
========================= */
const abrirTicket = async (ticket: any) => {
  ticketActivo.value = ticket

  const res = await fetch(
    `http://127.0.0.1:8000/api/tickets/${ticket.id}/comentarios/`
  )

  comentarios.value = await res.json()
}

/* =========================
   CREAR COMENTARIO
========================= */
const crearComentario = async () => {
  if (!ticketActivo.value) return

  errorComentario.value = ''

  if (!nuevoComentario.value.texto || nuevoComentario.value.texto.trim() === '') {
    errorComentario.value = 'El comentario es obligatorio'
    return
  }

  await fetch(
    `http://127.0.0.1:8000/api/tickets/${ticketActivo.value.id}/comentarios/`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(nuevoComentario.value)
    }
  )

  nuevoComentario.value = { autor: '', texto: '' }

  ticketActivo.value = null
  comentarios.value = []
}
</script>

<template>
<div class="container py-4">

  <div class="row g-4">

    <!-- FORMULARIO -->
    <div class="col-md-4">

      <div class="card shadow-sm border-0">
        <div class="card-body">

          <h4 class="mb-3 fw-bold">
            {{ modo === 'crear' ? '➕ Crear ticket' : '✏️ Editar ticket' }}
          </h4>

          <input v-model="nuevo.titulo" class="form-control mb-3" placeholder="Título" />

          <textarea v-model="nuevo.descripcion" class="form-control mb-3" rows="3" placeholder="Descripción"></textarea>

          <select v-model="nuevo.estado" class="form-select mb-3">
            <option value="no_empezado">No empezado</option>
            <option value="en_proceso">En proceso</option>
            <option value="completado">Completado</option>
          </select>

          <select v-model="nuevo.prioridad" class="form-select mb-3">
            <option value="baja">Baja</option>
            <option value="media">Media</option>
            <option value="alta">Alta</option>
          </select>

          <button class="btn btn-primary w-100 py-2 fw-semibold" @click="guardarTicket">
            {{ modo === 'crear' ? 'Crear ticket' : 'Guardar cambios' }}
          </button>

        </div>
      </div>

      <!-- COMENTARIOS DEBAJO DEL FORMULARIO -->
      <div v-if="ticketActivo" class="card shadow-sm border-0 mt-3">
        <div class="card-body">

          <h5 class="fw-bold mb-2">💬 Ticket seleccionado</h5>

          <p class="mb-1"><b>{{ ticketActivo.titulo }}</b></p>
          <p class="text-muted">{{ ticketActivo.descripcion }}</p>

          <hr />

          <h6>Comentarios</h6>

          <div v-if="comentarios.length === 0" class="text-muted small mb-2">
            Sin comentarios
          </div>

          <div v-for="c in comentarios" :key="c.id" class="mb-2">
            <b>{{ c.autor }}</b>
            <p class="mb-1">{{ c.texto }}</p>
          </div>

          <input
            v-model="nuevoComentario.autor"
            class="form-control mb-2"
            placeholder="Autor"
          />

          <textarea
            v-model="nuevoComentario.texto"
            class="form-control mb-1"
            placeholder="Comentario"
          ></textarea>

          <!-- ERROR -->
          <p v-if="errorComentario" class="text-danger small mb-2">
            {{ errorComentario }}
          </p>

          <button class="btn btn-primary w-100" @click="crearComentario">
            Enviar comentario
          </button>

        </div>
      </div>

    </div>

    <!-- LISTA -->
    <div class="col-md-8">

      <h4 class="fw-bold mb-3">📋 Tickets</h4>

      <div class="d-flex gap-2 mb-3">

        <select v-model="filtroEstado" class="form-select form-select-sm">
          <option value="todos">Todos estados</option>
          <option value="no_empezado">No empezado</option>
          <option value="en_proceso">En proceso</option>
          <option value="completado">Completado</option>
        </select>

        <select v-model="filtroPrioridad" class="form-select form-select-sm">
          <option value="todos">Todas prioridades</option>
          <option value="baja">Baja</option>
          <option value="media">Media</option>
          <option value="alta">Alta</option>
        </select>

      </div>

      <p v-if="loading" class="text-muted">Cargando...</p>

      <div v-else-if="ticketsFiltrados.length === 0" class="text-center text-muted mt-4">
        No hay tickets para mostrar
      </div>

      <div v-else>

        <div
          v-for="t in ticketsFiltrados"
          :key="t.id"
          class="card shadow-sm border-0 mb-3"
        >
          <div class="card-body">

            <div @click="abrirTicket(t)" style="cursor:pointer">

              <h5 class="fw-bold mb-1">{{ t.titulo }}</h5>
              <p class="text-muted small mb-2">{{ t.descripcion }}</p>

              <div class="mb-2">

                <span class="badge rounded-pill px-3 py-2 me-1 text-uppercase small"
                  :class="{
                    'bg-secondary': t.estado === 'no_empezado',
                    'bg-warning text-dark': t.estado === 'en_proceso',
                    'bg-success': t.estado === 'completado'
                  }">
                  {{ t.estado }}
                </span>

                <span class="badge rounded-pill px-3 py-2 text-uppercase small"
                  :class="{
                    'bg-success': t.prioridad === 'baja',
                    'bg-warning text-dark': t.prioridad === 'media',
                    'bg-danger': t.prioridad === 'alta'
                  }">
                  {{ t.prioridad }}
                </span>

              </div>

            </div>

            <div class="d-flex gap-2 mt-2">

              <button class="btn btn-outline-primary btn-sm" @click="editar(t)">
                ✏️ Editar
              </button>

              <button class="btn btn-outline-danger btn-sm" @click="eliminar(t.id)">
                🗑 Eliminar
              </button>

            </div>

          </div>
        </div>

      </div>

    </div>

  </div>

</div>
</template>