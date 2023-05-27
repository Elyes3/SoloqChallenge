import { createStore } from 'vuex'
import axios from 'axios'
export default createStore({
  state: {
    summoners : [],
  },
  getters: {
    getSummoners:(state) => state.summoners,
  },
  mutations: {
    setSummoners(state,value){
      state.summoners = value;
    }
  },
  actions: {
    fetchSummoners(state){
      axios({
        method :'get',
        url:'http://soloqchallengebackend.onrender.com/summoners'
      }).then(
         response =>{   
          state.commit('setSummoners',response.data);
        }
      )
    }
  },
})
