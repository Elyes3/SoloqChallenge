<template>
  <v-container fluid fill-height>
    <div class=" rounded-full shadow-1" v-if="summoners.length > 0">
    
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
          <div :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-white font-weight-bold d-flex justify-center align-center'">
            <img v-if="summoner && summoner.tier" :src="summoner.tier_image_url" class="tier" width="40" height="40"><img v-else class="tier" width="40" height="40" :src='`https://opgg-static.akamaized.net/images/medals_new/`+Tiers[tierRandom]+".png"'>&nbsp; {{ summoner && summoner.tier ? summoner.tier : Tiers[tierRandom].toUpperCase()  }}&nbsp;{{ summoner && summoner.tier ?  summoner.division : Math.floor(Math.random() * 4) + 1 }}
          </div>
        </td>
        <td :class="summoner && summoner.status === 'PENDING' ? 'pending' : ''">
          <div :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-white font-weight-bold text-center'">{{summoner && summoner.lp ? summoner.lp : 0 }}&nbsp;LP 
          <div class="d-flex justify-center items-center g-3" v-if="summoner && summoner.series"> 
            <span v-for="(serie,id) in summoner.series" :key="id" :class="(serie == 'W' ? 'blue-bg' : 'red-bg') + '  rounded-full wh-10 d-inline-block'">
            </span>       
            <span></span>
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
<WinrateGraph></WinrateGraph>
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
    toolTipColorChange(){
      const collection = document.getElementsByClassName('v-overlay__content');
      console.log(collection);
      for (let i = 0; i < collection.length; i++) {
        collection[i].setAttribute('style','background : #181936')
        console.log(collection[i]);
    }
    },
    onWidthChange1(newWidth) {
      console.log("td1:",newWidth)
      this.td1Height = newWidth;
    },
   generateHexColor(scaleValue) {
  // Interpolate RGB values based on the scale
  var red, green, blue;

  if (scaleValue < 50) {
    // Interpolate from red to orange
    red = Math.round((100 - scaleValue * 2) * 255 / 100);
    green = Math.round(scaleValue * 2 * 255 / 100);
    blue = 0;
  } else {
    // Interpolate from orange to blue
    red = 0;
    green = Math.round((150 - (scaleValue - 50) * 2) * 255 / 100);
    blue = Math.round(((scaleValue - 50) * 2 * 255 / 100));
  }

  // Convert RGB values to hexadecimal
  var hex = ((red << 16) | (green << 8) | blue).toString(16).padStart(6, '0');

  return '#' + hex;
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
  this.toolTipColorChange();
  const element = document.getElementById('row');
  const element1 = document.getElementById('td1');  
// Create a ResizeObserver to monitor width changes
const observer = new ResizeObserver(entries => {
  for (const entry of entries) {
    const newWidth = entry.contentRect.width;

    // Call a method or update a data property with the new width
    if(entry.target.id == 'row')
    this.onWidthChange(newWidth);
    else
    this.onWidthChange1(newWidth);
  }
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
</style>
