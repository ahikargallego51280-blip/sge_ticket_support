<template>
  <div class="container">
    <h1>Crear Ticket</h1>

    <form @submit.prevent="crearTicket">

      <div>
        <label>Título</label>
        <input v-model="form.titulo" required />
      </div>

      <div>
        <label>Descripción</label>
        <textarea v-model="form.descripcion" required></textarea>
      </div>

      <div>
        <label>Prioridad</label>
        <select v-model="form.prioridad">
          <option value="LOW">LOW</option>
          <option value="MEDIUM">MEDIUM</option>
          <option value="HIGH">HIGH</option>
          <option value="CRITICAL">CRITICAL</option>
        </select>
      </div>

      <button type="submit">Crear</button>
    </form>
  </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import api from "../api/axios";

const router = useRouter();

const form = reactive({
  titulo: "",
  descripcion: "",
  prioridad: "MEDIUM",
});

const crearTicket = async () => {
  try {
    await api.post("tickets/", form);
    router.push("/");
  } catch (err) {
    console.error(err);
  }
};
</script>