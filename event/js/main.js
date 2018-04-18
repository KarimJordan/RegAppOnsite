import Vue from 'vue'
// import SweetModal from '../../node_modules/sweet-modal-vue/src/plugin'
// import SweetModal from 'sweet-modal-vue/src/plugin.js'

//import eventList from './components/event-list.vue'
import eventForm from './components/event-form.vue'
import eventList from './components/event-list.vue'
import eventDetail from './components/event-detail.vue'
import eventDuplicate from './components/event-duplicate.vue'
import VModal from 'vue-js-modal'
import VuePaginate from 'vue-paginate'
import VueAlert from '@vuejs-pt/vue-alert'
import Simplert from 'vue2-simplert-plugin'
import VueNoty from 'vuejs-noty'

Vue.use(VueNoty, {
    layout: 'center',
    timeout: 500,
})
// Vue.use(Simplert)
Vue.use(VModal)
Vue.use(VuePaginate)
Vue.use(VueAlert)

new Vue({
    el: '#body',
    data: {
        count: ''
    },
    components: {
        eventList,
        eventForm,
        eventDetail,
        eventDuplicate
    }
})
