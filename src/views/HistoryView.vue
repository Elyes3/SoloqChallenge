<template>
    <div class="mt-16 pa-5 min-h-100">
<div class="min-h-100 d-flex flex-wrap justify-center items-center g-50" v-if="summoners">
<div v-for="summoner in summoners" :key="summoner.id">
  <v-card
    class="bg-lb rounded-lg h-100 d-flex flex-column"
    width="300"
  >
    <v-img
      :src="summoner.icon_url"
      height="200px"
      cover
    ></v-img>

    <v-card-title>
      {{ summoner.summoner }}
    </v-card-title>

    <v-card-subtitle class="d-flex flex-wrap g-10">
      <v-chip :style="'background:'+ tierColors[summoner.tier]">{{ summoner.tier }} {{ summoner.division }}</v-chip>
      <v-chip>{{ summoner.lp }} LP</v-chip>
      <v-chip v-if="summoner.is_hot_streak" style="background:green">Hot Streak</v-chip>
    </v-card-subtitle>
    <v-card-actions class="flex-auto">
      <v-btn
        color="blue-lighten-2"
        variant="text"
        class="ml-2"
      >
        Explore
      </v-btn>
    </v-card-actions>
  </v-card>
</div>
    </div>
    <div v-else class="min-h-100">
    <div class="text-center mt-16">
        <v-progress-circular
      indeterminate
      color="primary"
      ></v-progress-circular>

    </div>
</div>
</div>
</template>
<script>
export default {
    props:{
        summoners : {
            type : Array,
            required : true
        }
    },
    data(){
        return {
            tierColors:{
                IRON : "#a19d94",
                BRONZE : "#3E2723",
                SILVER : "#90A4AE",
                GOLD : "#FFC400",
                PLATINUM : "#00897B",
                DIAMOND : "#01579B",
                MASTER : "#450000",
                GRANDMASTER : "#450000",
                CHALLENGER : "#C4A15B"
            }
        }
    }
}
</script>
<style scoped>
    .bg-lb{
        background:#2f2f4d;
    }
    .g-50{
        gap:50px;
    }
    .g-10{
        gap:10px;
    }
</style>