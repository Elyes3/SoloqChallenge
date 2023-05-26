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
          KDA
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="summoner in summoners"
        :key="summoner.summoner_id"
      >
        <td class="align-center text-white font-weight-bold "><div class="d-flex align-center"><img v-if="summoner && summoner.icon_url" height="30" width="30" :src=summoner.icon_url class="rounded-img">&nbsp;<p>{{ summoner && summoner.summoner ? summoner.summoner : "UNKNOWN" }}</p></div></td>
        <td><div class="d-flex">
            <v-progress-linear :color="summoner && summoner.win && summoner.lose ? generateHexColor(Math.round(summoner.win*100/(summoner.win + summoner.lose))) : 0" :model-value="summoner && summoner.win && summoner.lose ? Math.round(summoner.win*100/(summoner.win + summoner.lose)) : 0" :height="19">
              <strong class="text-white">{{summoner && summoner.win && summoner.lose ? Math.round(summoner.win*100/(summoner.win + summoner.lose)) : 0}}%</strong>
            </v-progress-linear>
          </div>
      </td>
        <td>
        <div class="flex-gap-1">
          <div>
           <p class="text-white font-weight-bold">WAITING FOR MOST PLAYED</p>
          </div>
        </div>
      </td>
        <td>
          <div class="text-white font-weight-bold d-flex justify-center align-center">
            <img v-if="summoner && summoner.tier" :src="summoner.tier_image_url" class="tier" width="40" height="40">&nbsp; {{ summoner && summoner.tier ? summoner.tier : "" }}&nbsp;{{ summoner && summoner.tier ?  summoner.division : "" }}
          </div>
        </td>
        <td class="text-center text-white font-weight-bold">KDA</td>
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

</style>

<script>
import { VSkeletonLoader } from 'vuetify/labs/VSkeletonLoader'
export default{
  name: 'HelloWorld',
  components:{
    VSkeletonLoader
  },
  data: () => ({
    summoners1:[
      {
        name : "OBG Thanagor",
        icon : "https://ddragon.leagueoflegends.com/cdn/13.10.1/img/profileicon/1.png",
        wins : 300,
        losses : 302,
        mostPlayed : ['Pantheon','Mordekaiser','Sylas'],
        tier : 'Diamond 3',
        KDA : 1.84
      },
      {
        name : "OBG CakeSTD",
        icon : "https://ddragon.leagueoflegends.com/cdn/13.10.1/img/profileicon/1000.png",
        wins : 50,
        losses : 302,
        mostPlayed : ['Jinx','Kaisa','Caitlyn'],
        tier : 'Diamond 3',
        KDA : 3.03
      },
      {
        name : "OBG Ghost",
        icon : "https://ddragon.leagueoflegends.com/cdn/13.10.1/img/profileicon/753.png",
        wins : 25,
        losses :2,
        mostPlayed : ['LeeSin','Gragas','JarvanIV'],
        tier : 'Challenger',
        KDA : 10.84
      },
      {
        name : "godofmage",
        icon : "https://ddragon.leagueoflegends.com/cdn/13.10.1/img/profileicon/933.png",
        wins : 5,
        losses : 302,
        mostPlayed : ['Kled','Twitch','Singed'],
        tier : 'Iron 3',
        KDA : 2.5
      }
    ],
      }),

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
