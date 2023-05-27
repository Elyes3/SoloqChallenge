<template>
  <v-container fluid fill-height>
    <div class="rounded p-5" v-if="summoners.length > 0">
    
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
        class="position-relative"
      >
      
        <td class="align-center text-white font-weight-bold">
          <div class="d-flex align-center">
            <img v-if="summoner && summoner.icon_url" height="30" width="30" :src=summoner.icon_url class="rounded-img">
            <img v-else height="30" width="30" src="https://opgg-static.akamaized.net/meta/images/profile_icons/profileIcon1.jpg" class="rounded-img" >
            &nbsp;&nbsp;<p>{{ summoner && summoner.summoner ? summoner.summoner : "UNKNOWN" }}</p>
            <v-chip v-if="summoner.status === 'PENDING'"
      class="ma-2"
      color="light-blue">Pending</v-chip>
            <v-icon v-if="summoner && summoner.is_hot_streak && summoner.is_hot_streak == true" size="20" color="orange" icon="mdi-fire"></v-icon>
          </div>
        </td>
        <td>
          <div :class='summoner.status === "PENDING" ? "blureffect d-flex" : "d-flex"'>
            <v-progress-linear :color="summoner && summoner.win && summoner.lose ? generateHexColor(Math.round(summoner.win*100/(summoner.win + summoner.lose))) : generateHexColor(getRandomInt)" :model-value="summoner && summoner.win && summoner.lose ? Math.round(summoner.win*100/(summoner.win + summoner.lose)) : getRandomInt" :height="19">
              <strong class="text-white">{{summoner && summoner.win && summoner.lose ? Math.round(summoner.win*100/(summoner.win + summoner.lose)) : getRandomInt }}%</strong>
            </v-progress-linear>
          </div>
      </td>
        <td>
        <div class="flex-gap-1">
          <div :class='summoner.status === "PENDING" ? "blureffect" : ""'>
           <p class="text-white font-weight-bold">WAITING FOR MOST PLAYED</p>
          </div>
        </div>
      </td>
        <td>
          <div :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-white font-weight-bold d-flex justify-center align-center'">
            <img v-if="summoner && summoner.tier" :src="summoner.tier_image_url" class="tier" width="40" height="40"><img v-else class="tier" width="40" height="40" :src='`https://opgg-static.akamaized.net/images/medals_new/`+Tiers[tierRandom]+".png"'>&nbsp; {{ summoner && summoner.tier ? summoner.tier : Tiers[tierRandom].toUpperCase()  }}&nbsp;{{ summoner && summoner.tier ?  summoner.division : Math.floor(Math.random() * 4) + 1 }}
          </div>
        </td>
        <td>
          <div :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-white font-weight-bold text-center'">{{summoner && summoner.lp ? summoner.lp : 0 }}&nbsp;LP 
          <div class="d-flex justify-center items-center g-3" v-if="summoner && summoner.series"> 
            <span v-for="(serie,id) in summoner.series" :key="id" :class="(serie == 'W' ? 'blue-bg' : 'red-bg') + '  rounded-full wh-10 d-inline-block'">
            </span>       
            <span></span>
          </div>
        </div>
        </td>
        <td :class="(summoner.status === 'PENDING' ? 'blureffect' : '') + ' text-center text-white font-weight-bold'">{{(Math.random() *6).toFixed(2) }}</td>
      </tr>
    </tbody>
  </v-table>
</div>
<div v-else class="w-100">
  <v-skeleton-loader color="#2f2f4d" :elevation="24"></v-skeleton-loader>
</div>
</v-container>

</template>
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
.blureffect{
  -webkit-filter: blur(4px);
    -moz-filter: blur(4px);
    -o-filter: blur(4px);
    -ms-filter: blur(4px);
}
</style>

<script>
import { VSkeletonLoader } from 'vuetify/labs/VSkeletonLoader'
export default{
  name: 'HelloWorld',
  components:{
    VSkeletonLoader
  },
  data: () => ({
    Tiers : ['iron','bronze','silver','gold','platinum','diamond']
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
  onWidthChange(newWidth) {
      // Handle the width change here
      console.log('New width:', newWidth);
    }
  },
  props:{
    summoners:
    {
      type : Array,
      required : true,
    },
  },
  mounted(){

  }    
  }
</script>
