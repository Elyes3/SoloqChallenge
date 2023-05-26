
<template>
  <v-app class="min-h-100">
    <NavbarComponent></NavbarComponent>
    <CardComponent :text="text"></CardComponent>
    <HelloWorld/>
  </v-app>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'
import HelloWorld from './components/HelloWorld.vue';
import CardComponent from './components/CardComponent.vue';
export default{

  name: 'App',
  components:{
    NavbarComponent,HelloWorld,CardComponent
  },
  data(){
    return{
    text:{
      title : "SoloQ Challenge",
      p : "Tunisian players join an infernal fight in a soloQ climb full of surprises ! Check the ladder for more !"
    },
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
<style scoped>
.min-h-100{
  min-height: 90vh;
}
</style>