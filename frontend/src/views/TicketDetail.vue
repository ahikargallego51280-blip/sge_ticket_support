<template>
  <div v-if="ticket">
    <h1>{{ ticket.titulo }}</h1>

    <p><strong>Estado:</strong> {{ ticket.estado }}</p>
    <p><strong>Prioridad:</strong> {{ ticket.prioridad }}</p>
    <p><strong>Descripción:</strong> {{ ticket.descripcion }}</p>

    <hr>

    <h2>Comentarios</h2>

    <div v-if="ticket.comentarios?.length">
      <div
        v-for="c in ticket.comentarios"
        :key="c.id"
        style="border:1px solid #ccc; padding:10px; margin-bottom:10px;"
      >
        <strong>{{ c.autor }}</strong>
        <p>{{ c.texto }}</p>
      </div>
    </div>

    <div v-else>
      No hay comentarios
    </div>
  </div>

  <div v-else>
    Cargando ticket...
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import api from "../api/axios";

const route = useRoute();

const ticket = ref(null);

onMounted(async () => {
  try {
    const res = await api.get(`tickets/${route.params.id}/`);
    ticket.value = res.data;
  } catch (e) {
    console.error(e);
  }
});
</script>