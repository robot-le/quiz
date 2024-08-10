<template>
  <form @submit.prevent="register">
    <input v-model="username" type="text" placeholder="Username" required>
    <input v-model="password" type="password" placeholder="Password" required>
    <button type="submit">Register</button>
  </form>
</template>

<script>
import { ref } from 'vue'
import { useStore } from 'vuex'

export default {
  setup() {
    const store = useStore()
    const username = ref('')
    const password = ref('')

    const register = async () => {
      try {
        await store.dispatch('register', {
          username: username.value,
          password: password.value
        })
        // Redirect to login page or dashboard
      } catch (error) {
        console.error('Registration failed:', error)
      }
    }

    return { username, password, register }
  }
}
</script>