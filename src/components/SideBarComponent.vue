<template>
        <v-navigation-drawer
          class="bg-indigo-darken-5"
          theme="dark"
          permanent
          v-model="draw"
        >
        <div class="pa-5">
            <h1>Graph</h1>
            <v-select
                label="Select"
                :items="['Multikills', 'Elo','CS','Performance','Vision','Damage','KDA']"
                v-model="selected"
                @update:modelValue="emitNewData(selected)">
            </v-select>
        <div v-for="item in items[selected]" :key="item.id">
          <v-checkbox v-model="item.selected" :label="item.label"></v-checkbox>
        </div>
        </div>

        </v-navigation-drawer>
  </template>
  <style>
 .bg-indigo-darken-5{
    background-color:#2f2f4d !important;
 } 
  </style>
  <script>
  export default {
    props:{
        drawer:{
            type:Boolean,
            required:true,
        }
    },
    watch:{
        drawer: function(newVal){
            this.draw = newVal;
        },
        items:{
        handler(newItems)
        {
            console.log(newItems[this.selected])
            this.$emit('newCheck',newItems[this.selected])
        },
        deep : true,
    }
    },
    data(){
        return{
            draw : true,
            selected : 'Multikills',
            items:{ 
                Multikills:      
                        [
                            { id: 2, label: 'Two', selected: true },
                            { id: 3, label: 'Three', selected: false },
                            { id: 4, label: 'Four', selected: false },
                            { id: 5, label: 'Five', selected: false}
                        ],
                Performance:
                        [
                            {id: 1,label: 'ACE',selected: true},
                            {id: 2,label: 'MVP',selected: false}
                        ],
                Vision:
                        [
                            {id: 1,label: 'Wards Destroyed',selected: true},
                            {id: 2,label: 'Wards Placed',selected: false}
                        ],
                Damage:
                        [
                            {id: 1,label: 'To Champions',selected: true},
                            {id: 2,label: 'To Objectives',selected: false}
                        ],
                KDA:[       { id: 1, label: 'Kills', selected: true },
                            { id: 2, label: 'Deaths', selected: false },
                            { id: 3, label: 'Assists', selected: false },
                        ],

                CS : [{id: 1,label:'CS',selected : true}],
                Elo : [{id : 1,label : 'Elo',selected : true}]

            },
        }
    },
    methods:{
        emitNewData(value){
            this.$emit('newData',value)
            this.$emit('newCheck',this.items[value]);
        },
    },

  }
  </script>