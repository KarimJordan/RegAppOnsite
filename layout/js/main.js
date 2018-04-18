import Vue from 'vue'

//import eventList from './components/event-list.vue'
import layoutDetail from './components/layout-detail.vue'
import layoutForm from './components/layout-form.vue'

new Vue({
    el: '#body',
    data: {
        count: ''
    },
    components: {
        layoutDetail,
        layoutForm
    }
})

