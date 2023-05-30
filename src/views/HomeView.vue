<template>
    <div class="mt-16">
    <CardComponent :text="text"></CardComponent>
    <HelloWorld :summoners="$store.getters.getSummoners"/>
   </div>
</template>

<script>
import { defineComponent } from 'vue';

// Components
import HelloWorld from '../components/HelloWorld.vue';
import CardComponent from '@/components/CardComponent.vue';
export default defineComponent({
  name: 'HomeView',
  data(){
    return{
      text:{
      title : "SoloQ Challenge",
      p : "Tunisian players join an infernal fight in a soloQ climb full of surprises ! Check the ladder for more !"
    },
    }
  },
  components: {
    HelloWorld,CardComponent
  },
});
</script>
