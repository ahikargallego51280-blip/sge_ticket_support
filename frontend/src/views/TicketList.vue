<template>

<router-link to="/crear">Crear ticket</router-link>

  <div>
    <h1>Tickets</h1>

    <div v-if="loading">Cargando...</div>

    <ul v-else>
      <li v-for="t in tickets" :key="t.id">
        <router-link :to="`/tickets/${t.id}`">
          {{ t.titulo }}
        </router-link>

        - {{ t.estado }}
        - {{ t.prioridad }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import api from "../api/axios";

const tickets = ref([]);
const loading = ref(true);

onMounted(async () => {
  try {
    const res = await api.get("tickets/");
    tickets.value = res.data;
  } catch (e) {
    console.error(e);
  } finally {
    loading.value = false;
  }
});
</script>