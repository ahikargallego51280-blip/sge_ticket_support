import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

console.log("APP START")

const app = createApp(App)

console.log("BEFORE ROUTER")

app.use(router)

console.log("AFTER ROUTER")

app.mount('#app')

console.log("MOUNTED")