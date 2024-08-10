<script setup>
// import Navbar from './components/Navbar.vue';
// import { RouterView } from 'vue-router';

import { computed } from 'vue'
import { useStore } from 'vuex'
import Logout from '@/components/Logout.vue'

const store = useStore()
const isAuthenticated = computed(() => store.state.isAuthenticated)
</script>

<template>
  <!-- <Navbar /> -->
  <RouterView />
  <div id="app">
    <nav>
      <router-link to="/" v-if="!isAuthenticated">Home</router-link>
      <router-link to="/login" v-if="!isAuthenticated">Login</router-link>
      <router-link to="/register" v-if="!isAuthenticated">Register</router-link>
      <router-link to="/dashboard" v-if="isAuthenticated">Dashboard</router-link>
      <Logout v-if="isAuthenticated" />
    </nav>
    <router-view></router-view>
  </div>

</template>
