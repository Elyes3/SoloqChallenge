<template>
  <div class="bg-db mt-5 pa-3 rounded-full shadow-1">
    <div class="pa-5 d-flex justify-bet w-100 align-center">
      <div class="d-flex flex-column text-left">
      <h1 class="text-white">Winrate Graph</h1>
      <p>Add/Remove player's graph by clicking on his name</p>
      </div>
      <div>
        <v-btn-toggle rounded="xl" color="red" v-model="filterBy">
      <v-btn icon="mdi-gamepad" value="game" :class="filterBy == 'game' ? 'bg-blue' : 'bg-db'" @click="()=>{this.filterBy = 'game'}"></v-btn>
      <v-btn icon="mdi-clock" value="time" :class="filterBy == 'time' ? 'bg-blue' : 'bg-db'" @click="() => {this.filterBy = 'time'}"></v-btn>
    </v-btn-toggle>
      </div>
    </div>
    <div class=" bg-db rounded-100 mt-5 text-white he-100 bg-lblue">
      <Line :data="data" :options="options" />
    </div>
  </div>
</template>
<script>
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)
export default {
  components:{
    Line,
  },
  data(){
  return {
    filterBy : 'game',
  data:{

  labels: ['0 Games','10 Games', '20 Games', '30 Games', '40 Games', '50 Games', '60 Games', '70 Games','80 Games'],
  datasets: [
    {
      label: 'Romex Fortrex',
      backgroundColor: '#008080',
      data: [0,40, 66, 80, 90, 75, 80, 82,85],
    },
    {
      label: 'Ghosτ',
      backgroundColor: '#48BCD1',
      data: [0,85, 80, 90, 75, 80, 70, 65,60],
    },
    {
      label: 'OBG Thanagor',
      backgroundColor: '#333333',
      data: [0,90,82,76,81,72,67,71,75],
    },
    {
      label: 'OBG BotGapped',
      backgroundColor: '#32CD30',
      data: [0,75,90,81,85,87,89,91,80,90],
    },
    {
      label: 'Aikatsuyuri',
      backgroundColor: 'red',
      data: [0,60,70,65,50,60,63,70,68,73],
    },
    {
      label: 'Ekkonomics',
      backgroundColor: 'pink',
      data: [0,20,35,40,45,50,55,60,70],
    },
  ],
  },
  options :
  {
  responsive: true,
  maintainAspectRatio: false,
  elements:{
    line:{
    borderColor :'white',
    }
  },
  scales: {
        y: {
          ticks: {
            color: 'white',
            font : {
              family : 'MarkPro',
              weight : 'bold'
            }
          },
          title: {
            display: true,
            color : 'white',
            text: 'Winrate',
            font: {
              family: 'MarkPro',
              size: 14,
              weight: 'bold'
            }
            },
        },
        x:{
          ticks : {
            color :'white',
            font : {
              family : 'MarkPro',
              weight : 'bold'
            },
          },
          title: {
            display: true,
            color : 'white',
            text: 'Number of games',
            font: {
              family: 'MarkPro',
              size: 14,
              weight: 'bold'
            }
            },
        }
      },
  plugins: {
        legend: {
          labels: {
            color: 'white', // Set the text color
            font : {
              family : 'MarkPro',
              weight : 'bold'
            }
          },
        },
      },
  }
  
  }
  },
}
</script>
<style scoped>
    .he-100{
      height:50rem;
    }
    .rounded-100{
  border-radius : 10px;
  }
  .rounded-full{
    border-radius:25px;
  }
  .justify-bet{
    justify-content:space-between }
  .bg-db{
    background-color:#181936;
    color: white;
  }
  .shadow-1{
    box-shadow: 0px 0px 10px 0px black;
    border-radius:20px;
}
@font-face { 
  font-family: MarkPro; 
	src: url('../../public/MarkPro.otf'); } 
</style>