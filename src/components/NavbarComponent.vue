<template>
  
      <v-toolbar color="#0A0820" class="position-fixed z-index-9999">
        <v-app-bar-nav-icon v-if="this.$route.name === 'Graph'" variant="text" @click.stop="setDrawer"></v-app-bar-nav-icon>
        <router-link to="/" class="text-decoration-none">
          <div class="d-flex">
              <img src="logo.svg" width="60" height="60" class="ml-3 mr-2">
          </div>
        </router-link>
        <!-- Navbar content here -->
        <v-spacer></v-spacer>
        <router-link to="/graphs" class="text-decoration-none mr-4">Graphs</router-link>
        <router-link to="/history" class="text-decoration-none mr-4">History</router-link>
        <router-link to="/rules" class="text-decoration-none mr-4">Rules</router-link>
        <v-icon icon="mdi-theme-light-dark" class="me-5 text-white"></v-icon>
      </v-toolbar>
  </template>
<style>
.text-lb{
  color:#70d4dc;
}
.z-index-9999{
  z-index:9999
}
</style>
<script>
export default{
  methods:{
    setDrawer(){
      this.$store.commit('setDrawer');
    }
  }
}
</script>
  