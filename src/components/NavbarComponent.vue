<template>
  
      <v-toolbar color="#0A0820">
        <router-link to="/" class="text-decoration-none">
          <div class="d-flex">
              <img src="logo.svg" width="60" height="60" class="ml-3 mr-2">
          </div>
      </router-link>
        <!-- Navbar content here -->
  
        <v-spacer></v-spacer>
        <router-link to="/rules" class="text-decoration-none mr-4">Rules</router-link>
        <v-icon icon="mdi-theme-light-dark" class="me-5 text-white"></v-icon>
      </v-toolbar>
  </template>
<style>
.text-lb{
  color:#70d4dc;
}
</style>
  