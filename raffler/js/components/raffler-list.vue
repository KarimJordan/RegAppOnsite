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
                        <center><h4>E-Raffler</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <center>
            <form method="POST">
                <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                <button class="btn btn-block btn-create-event btn-ignore" type="submit">
                    NEW RAFFLE
                </button>
            </form>
        </center>

        <div class="container" v-for="(raffle, index) in raffles">
            <div :class="check_finished(raffle.num_of_draws, raffle.num_of_draws_done)">
                <div class="row">
                    <div class="col-sm-3 raffle-img-thumb">
                        <img :src="raffle.prize_image">
                    </div>
                    <div class="col-sm-7">
                        <h3>{{raffle.title}}</h3>
                        <table class="table">
                            <thead>
                            <th>Prize</th>
                            <th>QTY</th>
                            </thead>
                            <tr>
                                <td><h2>{{raffle.label}}</h2></td>
                                <td><h2>{{raffle.num_of_draws_done}}/{{raffle.num_of_draws}}</h2></td>
                            </tr>
                            <tr>
                                <td><a :href="'/rafflers/' + raffle.id + '/raffle_participants/'"><h4>View List</h4></a>
                                </td>
                                <td><a :href="'/rafflers/' + raffle.id + '/raffle_winners/'"><h4>View Winners</h4></a>
                                </td>
                            </tr>
                        </table>
                    </div>
                    <div class="col-sm-2">
                        <h5>Actions</h5>
                        <a @click="play_raffle(raffle.id)" class="actions-icon" data-toggle="tooltip"
                           data-original-title="Add more controls"><i
                                class="glyphicon glyphicon-play"></i></a>

                        <a @click="copy_raffle(raffle.id)" class="actions-icon btn-settings"
                           data-toggle="tooltip"
                           data-original-title="Add more controls">
                            <i class="glyphicon glyphicon-duplicate"></i></a>

                        <form :id="'raffle_form-' + raffle.id" :action="/rafflers/ + raffle.id + '/'">
                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                            <input type="hidden" name="_method" value="put">
                            <a @click="update_raffle(raffle.id)" class="actions-icon btn-settings">
                                <span class="glyphicon glyphicon-cog"></span>
                            </a>
                        </form>
                        

                        <form id="delete_form" class="delete-btn-form" :action="'/rafflers/' + delete_id + '/'" method="POST">
                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                            <input type="hidden" name="_method" value="delete"/>
                            <button @click="show_delete_modal(index)" class="actions-icon icn-delete-style event-delete-btn"
                                    type="button">
                                <span class="glyphicon glyphicon-trash" alt="Delete Record"></span>
                            </button>
                        </form>

                    </div>
                </div>
            </div>
        </div>

        <modal name="modal_delete" :height="200">
            <div class="modal-content">
                <div class="modal-header">
                    <h4>ARE YOU SURE YOU WANT TO DELETE?</h4>
                </div>
                <div class="modal-body" style="padding: 20px">
                    <center>
                        <ul class="list-inline ul-button">
                            <li>
                                <button class="btn btn-delete-yes " type="button" @click="delete_modal">YES</button>
                            </li>
                            <li>
                                <button class="btn btn-delete-no" type="button" @click="hide_modal">CANCEL </button>
                            </li>
                        </ul>
                    </center>
                </div>
            </div>
        </modal>

    </div>
</template>
<style>
    .modal-body {
        padding: 20px !important;
    }

    .v--modal-overlay {
        background: rgba(0, 0, 0, 0.5);
    }
</style>
<script type="text/babel">

    import axios from 'axios'

    export default {
        name: 'RafflerList',
        data() {
            return {
                raffles,
                event_id,
                csrf,
                delete_id: ''
            }
        },
        methods: {
            delete_modal(){
                let delete_form = document.getElementById('delete_form')
                delete_form.action =
                delete_form.submit()
            },
            hide_modal(){
                this.$modal.hide('modal_delete')
            },
            show_delete_modal(index){
                this.delete_id = this.raffles[index].id
                this.$modal.show('modal_delete')
            },
            check_finished(draw_num, draw_done) {
                if (draw_num == draw_done) {
                    return 'raffler-box-gray'
                } else {
                    return 'raffler-box'
                }
            },
            copy_raffle(id) {
                let url = '/rafflers/' + id + '/copy_raffle/'
                const request = {
                    method: 'post',
                    url: url,
                    headers: {'X-CSRFToken': this.csrf}
                }
                let that = this
                axios(request)
                    .then((response) => {
                        that.raffles = response.data.results
                    })
                    .catch((error) => {
                        console.log(error)
                    })

            },
            play_raffle(id) {
                window.open('/rafflers/' + id + '/play_raffle/', 'Play', "toolbar=no,menubar=no,scrollbars=no,resizable=no,location=no,directories=no,status=no,fullscreen=yes")
            },
            update_raffle(id) {
                let update_raffle = document.getElementById('raffle_form-' + id)
                update_raffle.setAttribute("method", "post")
                update_raffle.submit()
            }
        }
    }
</script>