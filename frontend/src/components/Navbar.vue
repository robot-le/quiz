<script>
export default {
  data() {
    return {
      foo: 'foo variable'
    }
  },
  methods: {
    isLogged() {
      // return true
      return false
    },
    async logout() {
      await authService.logout();
      this.$router.push({ name: 'Login' });
    }
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

        <template v-if="isLogged()">
        <li class="nav-item"><a href="#" class="nav-link disabled">spacekiddo</a></li>
        <div class="vr"></div>
        <li class="nav-item"><a href="#" class="nav-link">Logout</a></li>
        </template>
        <template v-else>
        <li class="nav-item"><a href="/login" class="nav-link">Login</a></li>
        <li class="nav-item"><a href="#" class="nav-link">Register</a></li>
        </template>


      </ul>
    </header>
  </div>

</template>
