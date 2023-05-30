import { createStore } from 'vuex'
import axios from 'axios'
export default createStore({
  state: {
    summoners : [],
    drawer : true,
  },
  getters: {
    getSummoners:(state) => state.summoners,
    getDrawer:(state) => state.drawer,
  },
  mutations: {
    setSummoners(state,value){
      state.summoners = value;
    },
    setDrawer(state){
      state.drawer = !state.drawer; 
    }
  },
  actions: {
    fetchSummoners(state){
      axios({
        method :'get',
        url:'https://soloqchallengebackend.onrender.com/summoners'
      }).then(
         response =>{   
          state.commit('setSummoners',response.data);
        }
      )
    }
  },
})
