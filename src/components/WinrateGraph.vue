<template>
  <div>
    <div class=" bg-db rounded-100 mt-5 text-white he-100 bg-lblue">
      <component :is="component" :data="data" :options="options" />
    </div>
  </div>
</template>
<script>
import { Line,Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  BarElement,
  Legend,
  
} from 'chart.js'
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
)
export default {
  components:{
    Line,
    Bar
  },
  props:{
    data : {
      required : true,
      type : Object
    },
    options :{
      required: true,
      type : Object,
    },
    component:{
      required : true,
      type : String,
    }
  }
}
</script>
<style scoped>
    .he-100{
      height:50rem;
    }
@font-face { 
  font-family: MarkPro; 
	src: url('../../public/MarkPro.otf'); } 
</style>