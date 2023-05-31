<template>
    <div class="min-h-100">
        <div class="d-flex justify-center pa-5 align-center min-h-100">
                
            <v-row no-gutters class="bg-lb pa-5 bg-lb rounded-xl">
                <v-col cols="12" md="6" class="d-flex justify-center items-center flex-column">
                    <div class="bg-lb pa-5">
                    <div class="mb-8 ">
                    <h1>THIS PAGE DOESN'T EXIST</h1>
                    You are lost. Just like in your <span class="text-blue">SoloQ games</span> !
                    You can either go back or look for a page that exists.
                    </div>
                    <v-divider></v-divider>
                    <button class="button-glitch"><v-icon icon="mdi-arrow-left"></v-icon>Back</button>
                    </div>
                </v-col>
                <v-col cols="12" md="6">
                <div class="d-flex justify-center align-center">
                    <img src="/404Err.png" width="500" height="500">
                </div>
                </v-col>
            </v-row>
        </div>
    </div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
.button-glitch,
.button-glitch:after {
  width: 100px;
  height: 40;
  line-height: 78px;
  font-size: 20px;
  background: linear-gradient(45deg, transparent 5%, rgb(10, 8, 32) 5%);
  border: 0;
  color: #fff;
  letter-spacing: 3px;
  box-shadow: 6px 0px 0px #00E6F6;
  outline: transparent;
  position: relative;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

.button-glitch:after {
  --slice-0: inset(50% 50% 50% 50%);
  --slice-1: inset(80% -6px 0 0);
  --slice-2: inset(50% -6px 30% 0);
  --slice-3: inset(10% -6px 85% 0);
  --slice-4: inset(40% -6px 43% 0);
  --slice-5: inset(80% -6px 5% 0);
  
  content: 'NOTFOUND';
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(45deg, transparent 3%, #00E6F6 3%, #00E6F6 5%, rgb(10, 8, 32) 5%);
  text-shadow: -3px -3px 0px #01176d, 3px 3px 0px #00E6F6;
  clip-path: var(--slice-0);
}

.button-glitch:hover:after {
  animation: 1s glitch;
  animation-timing-function: steps(2, end);
}

@keyframes glitch {
  0% {
    clip-path: var(--slice-1);
    transform: translate(-20px, -10px);
  }
  10% {
    clip-path: var(--slice-3);
    transform: translate(10px, 10px);
  }
  20% {
    clip-path: var(--slice-1);
    transform: translate(-10px, 10px);
  }
  30% {
    clip-path: var(--slice-3);
    transform: translate(0px, 5px);
  }
  40% {
    clip-path: var(--slice-2);
    transform: translate(-5px, 0px);
  }
  50% {
    clip-path: var(--slice-3);
    transform: translate(5px, 0px);
  }
  60% {
    clip-path: var(--slice-4);
    transform: translate(5px, 10px);
  }
  70% {
    clip-path: var(--slice-2);
    transform: translate(-10px, 10px);
  }
  80% {
    clip-path: var(--slice-5);
    transform: translate(20px, -10px);
  }
  90% {
    clip-path: var(--slice-1);
    transform: translate(-10px, 0px);
  }
  100% {
    clip-path: var(--slice-1);
    transform: translate(0);
  }
}

@media (min-width: 768px) {
  .button-glitch,
  .button-glitch:after {
    width: 140px;
    height: 86px;
    line-height: 88px;
  }
}

</style>