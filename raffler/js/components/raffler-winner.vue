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
                    <center><h4>Raffle Winners</h4></center>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="container-box">

                <div class="row">
                    <div class="col-sm-12">
                        <ul class="list-inline">
                            <li class="pull-right">
                                <input v-model="search" type="text" class="form-control"
                                       placeholder="search">
                            </li>
                        </ul>
                    </div>
                </div>
                <paginate name="winner_list"
                          :list="winner_list"
                          :per="10">
                    <div class="row">
                        <table class="table main-table winner-table">
                            <thead>
                            <th v-for="field in guest_fields">{{field.field_name}}</th>
                            </thead>
                            <tbody>
                            <tr v-for="winner in paginated('winner_list')">
                                <td v-for="data in winner">{{data}}</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                </paginate>
                <paginate-links for="winner_list"
                                :show-step-links="true" :async="true"></paginate-links>
            </div>
        </div>
    </div>
</template>
<style>
    .paginate-links.winner_list {
        margin: 0;
        padding-top: 20px;
        list-style: none;
    }

    .paginate-links.winner_list li {
        font-size: 14px;
        display: inline-block;
    }

    .paginate-links.winner_list a {
        float: left;
        cursor: pointer;
        padding: 8px 16px;
        text-decoration: none;
    }

    .paginate-links.winner_list li.active a {
        font-weight: bold;
        border: 1px solid #B4d500;
        background-color: #B4d500;
    }
</style>
<script type="text/babel">

    import axios from 'axios'

    export default {
        name: 'RafflerWinner',
        data() {
            return {
                event_id,
                raffle_id,
                guest_fields,
                winner_list,
                csrf,
                search: '',
                paginate: ['winner_list'],
            }
        },
        watch: {
            search: function (val) {
                this.get_winner_list()
            }
        },
        methods: {
            get_winner_list() {
                let that = this
                let params = {
                    search: this.search
                }
                let url = '/rafflers/' + this.raffle_id + '/search_winners/'
                params = {params: params}
                axios.get(url, params).then((response) => {
                    that.winner_list = response.data.winner_list
                })
            }
        }
    }
</script>