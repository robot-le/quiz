<template>
  <div>
    <h1>Login</h1>
    <!-- <form @submit.prevent="login">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage">{{ errorMessage }}</p> -->
  </div>
</template>

<script>
// import authService from '@/services/auth';

// export default {
//   data() {
//     return {
//       username: '',
//       password: '',
//       errorMessage: ''
//     };
//   },
//   methods: {
//     async login() {
//       try {
//         await authService.login({ username: this.username, password: this.password });
//         this.$router.push({ name: 'TestAuth' });
//       } catch (error) {
//         this.errorMessage = 'Invalid login credentials';
//       }
//     }
//   }
// };
</script>
