<template>
<div class="pa-5">
    <v-row no-gutters class="shadow-1">
      <v-col
        cols="12"
        lg="6"
      >
    <div class="d-flex cols-2 bg-db pa-5 rounded-div text-white h-100 justify-center align-center bg-lblue">

            <div>
                <h1 class="text-center">{{ text.title }}</h1>
                <h4 class="text-center">{{  text.p }}</h4>
            </div>

        </div>
        
    </v-col>
    <v-col
        cols="12"
        lg="6"
      >
        <div class="col-1 rounded-div-l h-100">
            <v-img src="test2.png" class="rounded-div-l"></v-img>
        </div>
    
    </v-col>
</v-row>
<div class="mt-10 rounded-full bg-lblue pa-10 d-flex justify-center align-center flex-column text-white shadow-1">
<h1 class="text-center">Here is the time left for the challenge to start !</h1>
<Countdown class="mt-5" deadline="2023-07-15 00:00:00"  mainFlipBackgroundColor="#0A0820" secondFlipBackgroundColor='#272841' mainColor ="white" secondFlipColor ="white" labelColor="white"/>
</div>
</div>

</template>
<style scoped>
.h-10-rem{
    max-height:10rem;
}
.mh-100{
    max-height:100%;
    display: block;
}
.rounded-div {
  border-radius: 20px 0 0 20px;

}
.bg-lblue{
    background: #2f2f4d;
  }
.rounded-div-l {
  border-radius: 0px 20px 20px 0px;
  
}
@media only screen and (max-width: 1280px) {
    .rounded-div-l  {
    border-radius : 0 0 20px 20px;
  }
  
  .rounded-div  {
    border-radius : 20px 20px 0px 0px;
    background: #2f2f4d;
  }
}
.shadow-1{
    overflow-x: visible;
    z-index:9999;
    box-shadow: 0px 0px 10px 0px black;
    border-radius:20px;
}
.rounded-full{
  border-radius : 20px 20px 20px 20px;
}
</style>
<script>
import {Countdown} from 'vue3-flip-countdown'
export default{
    
  props : {
        text : Object,
    },
  components:{
    Countdown
  }
}
</script>