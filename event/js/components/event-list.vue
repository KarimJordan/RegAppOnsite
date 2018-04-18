<template>
    <div>
        <!--Header-->
        <!--<header class="header" role="banner">-->
        <!--<nav class="navbar navbar-default" role="navigation">-->
        
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
        <!--</nav>-->
        <!--</header>-->

        <div class="sub-header" role="banner">
            <div class="container">
                <div class="sub-head-nav">
                    <nav class="sub-nav" role="navigation">
                        <center><h4>Events</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <div class="event-list container">
            <div class="row">
                <div class="col-sm-12">

                    <!--Events List-->
                    <div class="table-scrollable">
                        <table class="table table-striped">
                            <thead class="thead-inverse">
                            <tr class="table-active bg-main">
                                <th>Event</th>
                                <th>Venue</th>
                                <th>Start Date</th>
                                <th>End Date</th>
                                <!--<th>Email Template</th>-->
                                <th>GUEST</th>
                                <th col="1"></th>
                            </tr>
                            </thead>
                            <tbody>
                            <!--<tr>{{events}}</tr>-->

                            <tr v-for="event in events">
                                <td><a :href="event.id + '/'">{{ event.name }}</a></td>
                                <td>{{ event.venue }}</td>
                                <td>{{ event.start_date }}</td>
                                <td>{{ event.end_date }} </td>
                                <!--<td></td>-->
                                <td>{{ event.no_of_guest}} GUEST</td>
                                <td>
                                    <form :action="/events/ + event.id + '/'" method="POST">
                                        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                        <button class="event-delete-btn" name="_method" value="delete" type="submit">
                                            <span class="icon icon-trash" alt="Delete Record"></span>
                                        </button>
                                        <!--<a v-on:click="deleteEVent">-->
                                        <!--<span class="icon icon-trash" alt="Delete Record">{{event.id}}</span>-->
                                        <!--</a>&nbsp;&nbsp;&nbsp;-->
                                    </form>
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>

                </div>
            </div>
        </div>


        <!--Create new Event page-->
        <center>
            <div class="button-edit">
                <div class="">
                    <form method="POST">
                        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                        <button class="btn btn-block btn-manage-event" type="submit">Create New Event</button>
                    </form>
                </div>
            </div>
        </center>
    </div>
</template>
<style>
    tr {
        font-size: 14px
    }

    .btn {
        font-size: 14px
    }
</style>
<style scoped>
    /*@import '../../../node_modules/bootstrap/dist/css/bootstrap.css';*/
    /*@import "../../../node_modules/bootstrap-vue/dist/bootstrap-vue.css";*/
</style>
<script type="text/babel">

//    import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown'
//    import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item'
//    import bDropdownDivider from 'bootstrap-vue/es/components/dropdown/dropdown-divider'

    export default {
        name: 'EventList',
        data() {
            return {
                events: events,
                count: count,
                csrf,
                user
            }
        },
        components: {
//            bDropdown, bDropdownItem, bDropdownDivider
        },
        methods: {
            deleteEVent() {
                let delete_form = document.getElementById('delete_form')
                delete_form.submit()
            }
        }
    }
</script>