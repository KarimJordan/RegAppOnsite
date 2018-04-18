<template>
    <div>
        <header class="header" role="banner">
            <nav class="navbar navbar-default nav-new">
                <div class="container">
                    <a class="logo pull-left" :href="/events/"><img :src="require('../../../main/img/logo.png')"></a>
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                    </div>
                    <div class="nav-local collapse navbar-collapse" id="myNavbar">
                      <ul class="nav navbar-nav navbar-right">
                       <li><a href="#"><span class="fa fa-calendar"></span>EVENTS</a></li>
                         <li class="logout"><a href="/logout/"><span class="icon icon-power"></span>Logout</a></li>
                      </ul>
                    </div>
            
                </div>
            </nav>
        </header>
        <!--Title-->
        <div class="sub-header" role="banner">
            <div class="container">
                <div class="sub-head-nav">
                    <nav class="sub-nav" role="navigation">
                        <center><h4>ADD GUEST</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <form method="post">
            <div class="container">
                <div class="guest-fields container-box">
                    <h3>GUEST DETAILS</h3>
                    <guest-info-cell :items="guest_fields" @input="setGuestinfoData">
                    </guest-info-cell>

                    <!--<div v-for="field in guest_fields" class="row">-->
                    <!--<div class="col-md-7 col-sm-7">-->
                    <!--<form-cell-->
                    <!--:placeholder="field.field_name"-->
                    <!--dateTitle=""-->
                    <!--type="input"-->
                    <!--:required="true"-->
                    <!--:autofocus="true"/>-->
                    <!--</div>-->
                    <!--</div>-->
                    <div class="row">
                        <div class="col-sm-12">
                            <ul class="list-inline">
                                <li>
                                    <button class="btn btn-block btn-create-event btn-ignore" type="button"
                                            @click="save">SAVE
                                    </button>
                                </li>
                                <li>
                                    <form :action="/events/  + event_id" method="get">
                                        <button class="btn btn-block btn-preview btn-ignore" type="submit">CANCEL
                                        </button>
                                    </form>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>
<script type="text/babel">

    import GuestInfoCell from './guest-info-cell.vue'
    import axios from 'axios'

    export default {
        name: "GuestForm",
        components: {GuestInfoCell},
        filters: {
            allcaps: function (value) {
                if (!value) return ''
                value = value.toString()
                return value.toUpperCase()
            }
        },
        data() {
            return {
                guest: guest,
                guest_info: '',
                event_id: event_id,
                guest_fields: guest_fields,
                csrf,
                guest_info_field: []
            }
        },
        watch: {
            guest_info_field: function (val) {
                this.guest_info_field = val
            }
        },
        methods: {
            setGuestinfoData(fields) {
                this.guest_info_field = fields
            },
            save() {
                let guest_data = {}
                guest_data = {
                    event_id: this.event_id,
                    type: 'Walk In',
                    code: '',
                    info_list: this.guest_info_field
                }

                const redirect = '/events/' + this.event_id + '/'
                const request = {
                    method: 'post',
                    url: '/guests/',
                    data: guest_data,
                    headers: {'X-CSRFToken': this.csrf}
                }

                axios(request)
                    .then((response) => {
//                        console.log(response)
                        window.location.replace(redirect);
                    })
                    .catch((error) => {
                        console.log(error)
                    })

            }
        }
    }
</script>