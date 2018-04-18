import Vue from 'vue'
import rafflerList from './components/raffler-list.vue'
import rafflerForm from './components/raffler-form.vue'
import rafflerPlay from './components/raffler-play.vue'
import rafflerWinner from './components/raffler-winner.vue'
import rafflerParticipant from './components/raffler-participant.vue'
import VuePaginate from 'vue-paginate'
import VueNoty from 'vuejs-noty'
import VModal from 'vue-js-modal'

Vue.use(VModal)
Vue.use(VuePaginate)
Vue.use(VueNoty, {
    layout: 'center',
    timeout: 500,
})

new Vue({
    el: '#body',
    data: {
        count: ''
    },
    components: {
        rafflerList, rafflerForm, rafflerPlay, rafflerWinner, rafflerParticipant
    }
})