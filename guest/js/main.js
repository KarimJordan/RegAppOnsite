import Vue from 'vue'

//import eventList from './components/event-list.vue'
import guestForm from './components/guest-form.vue'
import guestFieldsForm from './components/guest-fields-form.vue'
import VModal from 'vue-js-modal'

Vue.use(VModal)

new Vue({
    el: '#body',
    data: {
        count: ''
    },
    components: {
        guestForm,
        guestFieldsForm
    }
})