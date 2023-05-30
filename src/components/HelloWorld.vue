<template>
  <v-container fluid fill-height>
    <div class="rounded-full shadow-1" v-if="summoners.length > 0">
    
      <v-table class="bg-db">

    <thead>
      <tr>
        <th class="text-left text-white">
          Summoner Name
        </th>
        <th class="text-center text-white">
          Winrate
        </th>
        <th class="text-center text-white">
          Most Played
        </th>
        <th class="text-center text-white">
          Tier
        </th>
        <th class="text-center text-white">
          LP
        </th>
        <th class="text-center text-white">
          KDA
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="summoner in summoners"
        :key="summoner.summoner_id"
        id="row"
      >
      
        <td  class="align-center text-white font-weight-bold" id="td1">
          <div class="d-flex align-center">
            <img v-if="summoner && summoner.icon_url" height="30" width="30" :src=summoner.icon_url class="rounded-img">
            <img v-else height="30" width="30" src="https://opgg-static.akamaized.net/meta/images/profile_icons/profileIcon1.jpg" class="rounded-img" >
            &nbsp;&nbsp;
            <a :href="'https://euw.op.gg/summoner/username='+summoner.summoner" target="_blank" class="text-decoration-none hv-bl">      
              <v-tooltip id="tooltip"
        activator="parent"
        location="end"
        
      ><img width="30" height="30" src="/opgg.png"></v-tooltip>{{ summoner && summoner.summoner ? summoner.summoner : "UNKNOWN" }}</a>
           <v-chip v-if="summoner.status === 'PENDING'" variant="elevated"
      class="ma-2 position-sm-absolute font-weight-bold text-uppercase" :style="'left :' + (parseInt(this.rowHeight) - parseInt(this.td1Height))/1.46 + 'px;'"
      color="#121327">Pending</v-chip>
            <v-icon v-if="summoner && summoner.is_hot_streak && summoner.is_hot_streak == true" size="20" color="orange" icon="mdi-fire"></v-icon>
          </div>
        </td>
        <td :class="summoner && summoner.status === 'PENDING' ? 'pending' : ''">
          <div :class='summoner.status === "PENDING" ? "blureffect d-flex" : "d-flex"'>
            <v-progress-linear :color="summoner && summoner.win && summoner.lose ? generateHexColor(Math.round(summoner.win*100/(summoner.win + summoner.lose))) : generateHexColor(getRandomInt)" :model-value="summoner && summoner.win && summoner.lose ? Math.round(summoner.win*100/(summoner.win + summoner.lose)) : getRandomInt" :height="19">
              <strong class="text-white">{{summoner && summoner.win && summoner.lose ? Math.round(summoner.win*100/(summoner.win + summoner.lose)) : getRandomInt }}%</strong>
            </v-progress-linear>
          </div>
      </td>
        <td :class="summoner && summoner.status === 'PENDING' ? 'pending' : ''">
        <div class="flex-gap-1">
          <div :class='summoner.status === "PENDING" ? "blureffect" : ""'>
           <p class="text-white font-weight-bold">WAITING FOR MOST PLAYED</p>
          </div>
        </div>
      </td>
        <td :class="summoner && summoner.status === 'PENDING' ? 'pending' : ''">
          <div :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-white font-weight-bold d-flex align-center'">
            <v-row no-gutters>
            <v-col cols="6">
              <div class="d-flex align-center justify-end">
                
              <img v-if="summoner && summoner.tier" :src="summoner.tier_image_url" class="tier" width="40" height="40"><img v-else class="tier" width="40" height="40" :src='`https://opgg-static.akamaized.net/images/medals_new/`+Tiers[tierRandom]+".png"'>
              </div>
            </v-col>
            <v-col cols="6" class="d-flex">
            <div class="d-flex align-center justify-start ml-2">
            <p>
            {{ summoner && summoner.tier ? summoner.tier : Tiers[tierRandom].toUpperCase()  }}&nbsp;
            {{ summoner && summoner.tier ?  summoner.division : Math.floor(Math.random() * 4) + 1 }}
            </p>
            </div>
            </v-col>
            </v-row>
          </div>
        </td>
        <td :class="summoner && summoner.status === 'PENDING' ? 'pending' : ''">
          <div :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-white font-weight-bold text-center'">{{summoner && summoner.lp ? summoner.lp : 0 }}&nbsp;LP 
          <div class="d-flex justify-center items-center g-3" v-if="summoner && summoner.series">
            <span :class="(summoner.series.lose == 1 && summoner.series.win == 1 ? 'blue-bg' : summoner.series.win == 1 ? 'blue-bg' : summoner.series.lose == 1 ? 'red-bg' : 'bg-white') + ' rounded-full wh-10 d-inline-block'"></span>
            <span :class="(summoner.series.lose == 1 && summoner.series.win == 1 ? 'red-bg' : 'bg-white') + ' rounded-full wh-10 d-inline-block'"></span>    
            <span class="bg-white rounded-full wh-10 d-inline-block"></span>
          </div>
        </div>
        </td>
        <td :class="(summoner.status === 'PENDING' ? 'pending' : '') + ' text-center text-white font-weight-bold'"><div :class="summoner.status === 'PENDING' ? 'blureffect' : ''">{{(Math.random() *6).toFixed(2) }}</div></td>
      </tr>
    </tbody>
  </v-table>
</div>
<div v-else class="w-100">
  <v-skeleton-loader color="#2f2f4d" :elevation="24"></v-skeleton-loader>
</div>
<div class="bg-db mt-5 pa-3 rounded-full shadow-1">
    <div class="pa-5 d-flex justify-bet w-100 align-center">
      <div class="d-flex flex-column text-left">
      <h1 class="text-white">Winrate Graph</h1>
      <p>Add/Remove player's graph by clicking on his name</p>
      </div>
      <div>
        <v-btn-toggle rounded="xl" color="red" v-model="filterBy">
      <v-btn icon="mdi-gamepad" value="game" :class="filterBy == 'game' ? 'bg-blue' : 'bg-ddb'" @click="()=>{this.filterBy = 'game'}"></v-btn>
      <v-btn icon="mdi-clock" value="time" :class="filterBy == 'time' ? 'bg-blue' : 'bg-ddb'" @click="() => {this.filterBy = 'time'}"></v-btn>
    </v-btn-toggle>
      </div>
    </div>
<WinrateGraph :data="data" :options="options" component="Line"></WinrateGraph>
</div>
</v-container>

</template>
<script>
import { VSkeletonLoader } from 'vuetify/labs/VSkeletonLoader'
import WinrateGraph from './WinrateGraph.vue';
export default{
  name: 'HelloWorld',
  components:{
    VSkeletonLoader,
    WinrateGraph

  },
  data: () => ({
    Tiers : ['iron','bronze','silver','gold','platinum','diamond'],
    rowHeight : 0,
    td1Height: 0,
    filterBy: 'game',
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
      }),
  computed:{
    getRandomInt(){
      return Math.floor(Math.random() * 100);
    },
    tierRandom(){
      return Math.floor(Math.random()*6);
    }
  },
  methods :{
    onWidthChange(newWidth) {
      console.log("row:",newWidth)
      this.rowHeight = newWidth;
    },
    onWidthChange1(newWidth) {
      console.log("td1:",newWidth)
      this.td1Height = newWidth;
    },
  generateHexColor(scaleValue) {
  if (scaleValue < 45 ){
    return '#610101'
  }
  else if (scaleValue < 50)
  {
    return '#6b6b6b'
  }
  else if(scaleValue<60){
    return '#00BBA3';
  }
  else if (scaleValue<70){
    return '#0093FF'
  }
  else if (scaleValue<80)
  {
    return '#FF8200'
  }
  else
  {
    return '#FFD700'
  }
},
  getTier(tier){
    return tier.split(' ')[0];
  },

},
  props:{
    summoners:
    {
      type : Array,
      required : true,
    },
  },
  updated(){
  const element = document.getElementById('row');
  const element1 = document.getElementById('td1');  
// Create a ResizeObserver to monitor width changes
const observer = new ResizeObserver(entries => {
  window.requestAnimationFrame(() =>{
  for (const entry of entries) {
    const newWidth = entry.contentRect.width;

    // Call a method or update a data property with the new width
    if(entry.target.id == 'row')
    this.onWidthChange(newWidth);
    else
    this.onWidthChange1(newWidth);
  }
})
});

// Start observing the element
observer.observe(element);
observer.observe(element1)

  }    
  }
</script>
<style scoped>
.bg-db{
  background: #2f2f4d;
}
.bg-ddb{
  background:#151530;
}
@media only screen and (max-width: 1280px) {
    * {
    font-size:0.65rem;
    white-space: nowrap;
  }
  .tier{
    width:30px;
    height:30px;
  }

}
@media only screen and (min-width: 690px) {
.position-sm-absolute{
  position:absolute;
}
}
@media only screen and (max-width: 690px) {
.position-sm-absolute{
  position:initial;
  font-size:0.5rem;
}
}
@media only screen and (max-width: 690px) {
    * {
    font-size:0.55rem;
    white-space: nowrap;
  
  }
  .tier{
    width:30px;
    height:30px;
  }
}
.g-3{
  gap : 3px;
}
.wh-10{
  width:10px;
  height:10px;
}
.blue-bg{
  background-color: rgb(46, 175, 255);
}
.red-bg{
  background-color: rgb(244, 113, 113);
}
th{
  border-radius: 30px;
}
.rounded-full{
  border-radius: 20px;
  font-size:0.7rem;
    text-align: center;
    overflow: visible;
}
.flex-gap-1{
  display: flex;
  gap :9px;
  align-items: center;
  justify-content: center;
}
  .rounded-div  {
    border-radius : 20px 0px 0px 20px;
    font-size:0.7rem;
    text-align: center;
    overflow: visible;
  }
  .rounded-div-l {
  border-radius: 0px 20px 20px 0px;
  font-size:0.7rem;
  text-align: center;
  overflow: visible;
}
.rounded-img{
  border-radius: 25px;
}
.pdr-3{
padding-right:30px !important;
}
.pdl-3{
padding-right: 30px !important;
}
.wins{
  background:#4758EB;
}
.losses{
  background : rgb(250, 45, 86);
}
.wins-text{
  color:#4758EB;
  font-weight: bold;
  padding:3px;
  border-radius: 5px;
  background :#151530;
}
.text-gray{
  color:rgb(170, 170, 170);
}
.losses-text{
  color : rgb(250, 45, 86);
  font-weight:bold;
  padding:3px;
  border-radius: 5px;
  background :#151530;
}
td{
  width:20%;
}
.pending{
  background: transparent;
  background-color: #1c1c39ba
}
.blureffect{
  -webkit-filter: blur(4px);
    -moz-filter: blur(4px);
    -o-filter: blur(4px);
    -ms-filter: blur(4px);
    filter: blur(4px);
}
.shadow-1{
    box-shadow: 0px 0px 10px 0px black;
    border-radius:20px;
}
.hv-bl:hover{
color:#2196F3;
}

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
  .shadow-1{
    box-shadow: 0px 0px 10px 0px black;
    border-radius:20px;
}
@font-face { 
  font-family: MarkPro; 
	src: url('../../public/MarkPro.otf'); } 
</style>
