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
        
        <div class="sub-header" role="banner">
            <div class="container">
                <div class="sub-head-nav">
                    <nav class="sub-nav" role="navigation">
                        <center><h4>Multiple Entries</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <div class="container">
            <div class="event-details">
                <event-duplicate-cell
                        :csrf="csrf"
                        :event_id="event_id"
                        :fields="guest_fields"
                        :duplicates="duplicates_list"
                        :duplicate_info="guest_default_dict">
                </event-duplicate-cell>
            </div>
        </div>
    </div>
</template>
<script type="text/babel">

    import EventDuplicateCell from './event-duplicate-cell.vue'

    export default {
        name: 'EventDuplicate',
        components: {
            EventDuplicateCell
        },
        data() {
            return {
                event_id,
                guest_fields,
                guest_default_dict,
                duplicates_list,
                csrf
            }
        }
    }
</script>