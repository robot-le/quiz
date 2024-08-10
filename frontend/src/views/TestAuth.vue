<template>
  <div>
    <h1>Dashboard</h1>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
import authService from '@/services/auth';

export default {
  methods: {
    async logout() {
      await authService.logout();
      this.$router.push({ name: 'Login' });
    }
  }
};
</script>
