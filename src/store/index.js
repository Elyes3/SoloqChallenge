import { createStore } from 'vuex'
import axios from 'axios'
export default createStore({
  state: {
    summoners : null,
  },
  getters: {
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
        url:'https://soloqchallengebackend.onrender.com/summoners'
      }).then(
        response =>{

          state.setSummoners(state,response.data);
        }
      )
    }
  },
})
