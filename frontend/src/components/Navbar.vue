<script>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'


export default {
  data() {
    return {
      store: useStore()
    }
  },
  computed: {
    isAuthenticated() {
      return this.store.state.isAuthenticated;
    }
  },
  setup() {
    const store = useStore()
    const router = useRouter()

    const logout = async () => {
      try {
        await store.dispatch('logout')
        router.push('/login')
      } catch (error) {
        console.error('Logout failed:', error)
      }
    }

    return { logout }
  }
}
</script>

<template>
<div class="container">
    <header class="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
      <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-body-emphasis text-decoration-none">
        <span class="fs-4">quiz</span>
      </a>

      <ul class="nav nav-underline">
      </ul>

      <ul class="nav nav-pills">

        <template v-if="this.isAuthenticated">
        <li class="nav-item"><a href="#" class="nav-link disabled">{{ this.store.state.user.obj.username }}</a></li>
        <div class="vr"></div>
        <li class="nav-item"><a href="#" @click="logout" class="nav-link">Logout</a></li>
        </template>
        <template v-else>
        <li class="nav-item"><RouterLink to="/login" class="nav-link">Login</RouterLink></li>
        <li class="nav-item"><RouterLink to="/register" class="nav-link">Register</RouterLink></li>
        </template>


      </ul>
    </header>
  </div>

</template>
