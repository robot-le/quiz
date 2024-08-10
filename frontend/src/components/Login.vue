<!-- src/components/Login.vue -->
<template>
  <form @submit.prevent="login">
    <input v-model="username" type="text" placeholder="Username" required>
    <input v-model="password" type="password" placeholder="Password" required>
    <button type="submit">Login</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()
const username = ref('')
const password = ref('')

const login = async () => {
  try {
    await store.dispatch('login', {
      username: username.value,
      password: password.value
    })
    router.push('/dashboard')
  } catch (error) {
    console.error('Login failed:', error)
  }
}
</script>