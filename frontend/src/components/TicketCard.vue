<script setup lang="ts">
defineProps<{
  ticket: any
}>()

const emit = defineEmits(['eliminar'])

const eliminar = (id: number) => {
  emit('eliminar', id)
}
</script>

<template>
  <div style="border:1px solid #ccc; padding:10px; margin:10px; border-radius:8px;">
    <h3>#{{ ticket.id }} - {{ ticket.titulo }}</h3>

    <p>{{ ticket.descripcion }}</p>

    <p><b>Estado:</b> {{ ticket.estado }}</p>
    <p><b>Prioridad:</b> {{ ticket.prioridad }}</p>

    <button
      @click="eliminar(ticket.id)"
      style="background:red;color:white;padding:5px;border:none;border-radius:4px;"
    >
      🗑 Eliminar
    </button>
  </div>
</template>