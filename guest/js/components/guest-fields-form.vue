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
                            <li><a href="/events/"><span class="fa fa-calendar"></span>EVENTS</a></li>
                            <li class="logout"><a href="/logout/"><span class="icon icon-power"></span>Logout</a></li>
                        </ul>
                    </div>

                </div>
            </nav>
        </header>

        <div class="sub-header" role="banner">
            <div class="container">
                <div class="sub-head-nav">
                    <nav class="sub-nav" role="navigation">
                        <center><h4>MANAGE GUEST FIELD</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="guest-fields container-box">
                <h3>GUEST DETAILS</h3>
                <field-cell :items="guest_info_fields"
                            :event_id="event_id"
                            :required="true" @item_update="item_update"
                            @delete_item="delete_item" @set_hidden="set_hidden">
                </field-cell>
                <!--Add Custom Field-->
                <div class="custom-fields no-padding no-margin">
                    <div class="container">
                        <h4>ADD A CUSTOM FIELD</h4>
                        <br>
                        <div class="col-sm-12 no-padding add-c-field">
                            <ul class="list-inline">
                                <li>
                                    <input type="input" v-model="field_name" class="form-control" placeholder="LABEL"
                                           required autofocus>
                                </li>
                                <li>
                                    <button class="btn btn-block btn-add-field" type="button" @click="add_field">
                                        Add Field
                                    </button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!--Save Data to Guest Info Field table-->
                <ul class="list-inline">
                    <li>
                        <button @click="save_info" class="btn btn-block btn-create-event btn-ignore" type="submit">
                            SAVE
                        </button>
                    </li>
                    <li>
                        <form :action="/events/ + event_id" method="get">
                            <button class="btn btn-block btn-preview btn-ignore" type="submit"
                                    onclick="">CANCEL
                            </button>
                        </form>
                    </li>
                </ul>

            </div>
        </div>


    </div>
</template>
<script type="text/babel">

    import axios from 'axios'

    import FormCell from '../../../main/js/components/form-cell.vue'
    import FieldCell from './guest-field-cell.vue'

    export default {
        name: "GuestFieldsForm",
        components: {FormCell, FieldCell},
        data() {
            return {
                guest_info_fields: guest_info_fields,
                event_id: event_id,
                field_name: '',
                save_clicked: false,
                csrf
            }
        },
        methods: {
            item_update(val) {
                this.guest_info_fields = val
                const url = '/guests/' + this.event_id + '/udpate_order/'

                for (let index = 0; index < this.guest_info_fields.length; index++) {
                    console.log(this.guest_info_fields[index])

                    let data = {
                        event_id: this.event_id,
                        field_name: this.guest_info_fields[index].field_name,
                        id: this.guest_info_fields[index].id,
                        is_email: this.guest_info_fields[index].is_email,
                        is_hidden: this.guest_info_fields[index].is_hidden,
                        is_required: this.guest_info_fields[index].is_required,
                        is_resolved: this.guest_info_fields[index].is_resolved,
                        is_unique: this.guest_info_fields[index].is_unique,
                        order: index
                    }

                    let request = {
                        method: 'post',
                        url: url,
                        data: data,
                        headers: {'X-CSRFToken': this.csrf}
                    }

                    axios(request)
                        .then((response) => {
                            console.log(response)
//                        window.location.replace(redirect);
                        })
                        .catch((error) => {
                            console.log(error)
                        })
                }
            },
            call_request(data) {
                const redirect = '/guests/fields/' + this.event_id + '/'
                const request = {
                    method: 'post',
                    url: redirect,
                    data: data,
                    headers: {'X-CSRFToken': this.csrf}
                }

                axios(request)
                    .then((response) => {
                        console.log(response)
//                        window.location.replace(redirect);
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            set_hidden(position, id, event_id, field_name, hidden) {
                let data = {
                    'id': id,
                    'order': position,
                    'event_id': event_id,
                    'field_name': field_name,
                    'hidden': hidden,
                    'update_hidden': 'update_hidden'
                }
                this.call_request(data)
            },
            delete_item(position, id) {
                this.guest_info_fields.splice(position, 1)
                let data = {
                    'id': id,
                    'delete': 'delete'
                }
                this.call_request(data)
            },
            save_info() {
                let that = this
                this.save_clicked = true
                const redirect = '/events/' + this.event_id + '/'
                const request = {
                    method: 'post',
                    url: '/guests/fields/' + this.event_id + '/',
                    data: {
                        'guest_info_fields': this.guest_info_fields
                    },
                    headers: {'X-CSRFToken': this.csrf}
                }
                axios(request)
                    .then((response) => {
                        that.save_clicked = false
                        window.location.replace(redirect)
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            add_field() {
                this.guest_info_fields.push(
                    {
                        'field_name': this.field_name,
                        'event_id': this.event_id,
                        'order': this.guest_info_fields.length,
                        'is_required': false,
                        'is_unique': false,
                        'is_email': false,
                        'is_resolved': true,
                    }
                )

                let data = {
                    'field_name': this.field_name,
                    'event_id': this.event_id,
                    'order': this.guest_info_fields.length
                }

                this.call_request(data)

                this.field_name = ''
            },
        }
    }
</script>