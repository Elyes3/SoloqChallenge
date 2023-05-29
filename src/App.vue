
<template>
  <v-app class="min-h-100">
    <NavbarComponent></NavbarComponent>
    <router-view></router-view>
  </v-app>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
export default{

  name: 'App',
  components:{
    NavbarComponent
  },
  data(){
    return{

  }
},
  computed:{
    getSummoners(){
      return this.$store.getters.getSummoners
    }
  },
  methods:{
    setSummoners(){
      return this.$store.dispatch('fetchSummoners')
    },

  },
  mounted(){
    this.$store.dispatch('fetchSummoners')
  }
}
</script>
<style>
.min-h-100{
  min-height: 90vh;
}
@font-face { 
  font-family: MarkPro; 
	src: url('../public/MarkPro.otf'); } 
*{
font-family: 'MarkPro';
color:white;
}
</style>