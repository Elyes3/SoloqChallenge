<template>
    <div>
        <v-card>
        <v-layout>
            <Sidebar  @newData="setSelect" @newCheck="setData"  class="mt-16" :drawer="this.$store.getters.getDrawer"></Sidebar>
            <v-main style="min-height:100vh;background:#181936">
              <div>
                <div class=" bg-db rounded-100 mt-5 text-white he-100 bg-lblue mt-16">
                  <Bar v-if="text != 'Elo'" :key="this.text+this.value" :data="newData" :options="options"></Bar>
                  <Line v-else :data="dataLines" :options="optionsLine"></Line>
                </div>
              </div>
            </v-main>
        </v-layout>
        
        </v-card>
    </div>
</template>
<script>
import Sidebar from '../components/SideBarComponent.vue'
import graphData from '../../data/GraphData.json'
import { Bar,Line } from 'vue-chartjs'
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
    Sidebar,
    Bar,
    Line
},
    computed:{
      newData(){
        return this.data;
      }
    },
    methods:{
       setSelect(value){
        this.text=value;
        if(this.text == 'Elo')
          this.optionsLine.scales.x.title.text = 'Number of games';
        else
          this.options.scales.x.title.text = 'Players';
        this.options.scales.y.title.text = this.text;
        this.optionsLine.scales.y.title.text = this.text;
        this.data.datasets = [];
       },
       setData(value){
        this.value = value.filter(val => val.selected == true).length;
        if (value.length > 0 && value.length < 5){
          value.forEach(val => {
            if (val.selected == true){
            const exist = this.data.datasets.find(el=> el.label == val.label);  
            
            if(!exist){
            let valLabel = val.label.split(' ').join('') 
            const obj = {
              label : val.label,
              data : graphData.data[this.text][valLabel],
              backgroundColor : this.generateColor()
              
            }
            this.data.datasets.push(obj)            
            }
          }
            else if (val.selected == false)
            { 
              this.data.datasets = this.data.datasets.filter(dataset =>
                dataset.label !=  val.label)
            }

          })
        }
        else
          this.data.datasets = [];
      },
      generateColor() {
        const red = Math.floor(Math.random() * 101) + 100;
        const green = Math.floor(Math.random() * 101) + 100;
        const blue = Math.floor(Math.random() * 101) + 100;
        const hex = `#${red.toString(16)}${green.toString(16)}${blue.toString(16)}`;
        return hex;
}
    },  
    data(){
        return{
          value : 1,
          text : 'Multikills',
          images : [
            "https://opgg-static.akamaized.net/images/medals_new/iron.png",
            "https://opgg-static.akamaized.net/images/medals_new/bronze.png",
            "https://opgg-static.akamaized.net/images/medals_new/silver.png",
            "https://opgg-static.akamaized.net/images/medals_new/gold.png",
            "https://opgg-static.akamaized.net/images/medals_new/platinum.png",
            "https://opgg-static.akamaized.net/images/medals_new/diamond.png",
            "https://opgg-static.akamaized.net/images/medals_new/bronze.png",
            "https://opgg-static.akamaized.net/images/medals_new/grandmaster.png",
            "https://opgg-static.akamaized.net/images/medals_new/challenger.png"
],
          yLabels:{
            0: "Unranked",
            1: "Iron 4",
            2: "Iron 3",
            3: "Iron 2",
            4: "Iron 1",
            5: "Bronze 4",
            6: "Bronze 3",
            7: "Bronze 2",
            8: "Bronze 1",
            9: "Silver 4",
            10: "Silver 3",
            11: "Silver 2",
            12: "Silver 1",
            13: "Gold 4",
            14: "Gold 3",
            15: "Gold 2",
            16: "Gold 1",
            17: "Platinum 4",
            18: "Platinum 3",
            19: "Platinum 2",
            20: "Platinum 1",
            21: "Diamond 4",
            22: "Diamond 3",
            23: "Diamond 2",
            24: "Diamond 1",
            25: "Master",
            26: "Grandmaster",
            27: "Challenger"
          },
    data:{
      labels: ['Romex Fortrex','OBG BotGapped','Hou Max','OBG Logic','OBG Thanagor'],
      datasets: [{
        label : 'Two',
        data : [15,20,5,8,15],
        backgroundColor : '#ADD8E6'
      }]},
      dataLines :{
        labels : ['10 Games','20 Games','30 Games','40 Games','50 Games','60 Games','70 Games','80 Games'],
        datasets: [
  {
    label: 'Romex Fortrex',
    backgroundColor: '#008080',
    data: graphData.data.Elo['Romex Fortrex'],
  },
  {
    label: 'Hou Max',
    backgroundColor: '#48BCD1',
    data: graphData.data.Elo['Hou Max'],
  },
  {
    label: 'OBG Thanagor',
    backgroundColor: '#333333',
    data: graphData.data.Elo['OBG Thanagor'],
  },
  {
    label: 'OBG BotGapped',
    backgroundColor: '#32CD30',
    data: graphData.data.Elo['OBG BotGapped'],
  },
  {
    label: 'OBG Logic',
    backgroundColor: '#32CD30',
    data: graphData.data.Elo['OBG Logic'],
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
          beginAtZero : true,
          font : {
            family : 'MarkPro',
            weight : 'bold'
          }
        },
        title: {
          display: true,
          color : 'white',
          text: 'Multikills',
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
          text: 'Players',
          font: {
            family: 'MarkPro',
            size: 14,
            weight: 'bold'
          }
          },
      },
    },
    plugins:{
      tooltip: {
        titleFont:{
          weight:'bold',
          family:'MarkPro'
        },
        bodyFont:{
          weight:'bold',
          family:'MarkPro'
        },

      },
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
},
optionsLine :
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
          beginAtZero : true,
          callback: (value) => {
                    if(this.text == "Elo"){
                    // for a value (tick) equals to 8
                    return this.yLabels[value];
                    }
                    // 'junior-dev' will be returned instead and displayed on your chart
                },
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
    plugins:{
      tooltip: {
        callbacks:{
          label: tooltipItem => {
                    return tooltipItem.dataset.label + " : " + this.yLabels[parseInt(tooltipItem.raw)];
          }
        },
        titleFont:{
          weight:'bold',
          family:'MarkPro'
        },
        bodyFont:{
          weight:'bold',
          family:'MarkPro'
        },
        
      },
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
    }
}
</script>
<style>
        .he-100{
      min-height:90vh;
    }
</style>