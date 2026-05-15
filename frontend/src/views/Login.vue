<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const password = ref('')
const error = ref('')

const login = async () => {
  error.value = ''

  try {
    const res = await fetch('http://127.0.0.1:8000/api/token/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    })

    if (!res.ok) {
      error.value = 'Usuario o contraseña incorrectos'
      return
    }

    const data = await res.json()

    // Guardar tokens
    localStorage.setItem('access', data.access)
    localStorage.setItem('refresh', data.refresh)

    alert('Login correcto ✔️')

    // 🚀 REDIRECCIÓN CORRECTA (sin recargar la app)
    router.push('/tickets')

  } catch (err) {
    error.value = 'Error de conexión con el servidor'
  }
}
</script>

<template>
  <div class="container py-5" style="max-width: 400px">

    <h3 class="mb-3">Login</h3>

    <input
      v-model="username"
      class="form-control mb-2"
      placeholder="Usuario"
    />

    <input
      v-model="password"
      type="password"
      class="form-control mb-2"
      placeholder="Contraseña"
    />

    <button class="btn btn-primary w-100" @click="login">
      Entrar
    </button>

    <p v-if="error" class="text-danger mt-2">
      {{ error }}
    </p>

  </div>
</template>