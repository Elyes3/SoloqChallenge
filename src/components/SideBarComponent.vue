<template>
    <v-card>
      <v-layout>
        <v-navigation-drawer
          class="bg-indigo-darken-5"
          theme="dark"
          permanent
        >
        <v-select
            label="Select"
            :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']">

        </v-select>
        </v-navigation-drawer>
        <v-main style="min-height:100vh;background:#181936"></v-main>
      </v-layout>
    </v-card>
  </template>
  <style>
 .bg-indigo-darken-5{
    background-color:#2f2f4d !important;
 } 
  </style>