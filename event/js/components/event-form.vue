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
        <!--Create Event Header-->
        <div class="sub-header" role="banner">
            <div class="container">
                <div class="sub-head-nav">
                    <nav class="sub-nav" role="navigation">
                        <center><h4>CREATE EVENT</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <!--Event Info-->
        <form action="" method="POST" role="form">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
            <div class="container">
                <div class="event-details container-box">

                    <h3>Event Details</h3>
                    <div class="row">
                        <div class="col-sm-12">
                            <form-cell v-model="event.name" value="" title="Event Title*" dateTitle="" type="input"
                                       name="name"
                                       :required="true"
                                       :autofocus="true"/>
                        </div>
                        <div class="col-sm-12">
                            <form-cell v-model="event.venue" value="" title="Venue*" dateTitle="" type="input"
                                       name="venue"
                                       :required="true"
                                       :autofocus="true"/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-4 col-xs-4">
                            <h3>Start Date</h3>
                            <input type="hidden" name="start_date" :value="start_date"/>
                            <div class="form-group">
                                <input type="text" class="form-control" id="start_date" required>
                            </div>
                        </div>
                        <div class="col-md-4 col-xs-4">
                            <h3>Start Time</h3>
                            <div class="timewrapper form-group">
                                <vue-timepicker v-model="start_time" format="hh:mm a" :minute-interval="5"
                                                hide-clear-button required></vue-timepicker>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-4 col-xs-4">
                            <h3>End Date</h3>
                            <input type="hidden" name="end_date" :value="end_date"/>
                            <div class="form-group">
                                <input type="text" class="form-control" id="end_date" required>
                            </div>
                        </div>
                        <div class="col-md-4 col-xs-4">
                            <h3>End Time</h3>
                            <div class="timewrapper">
                                <vue-timepicker v-model="end_time" format="hh:mm a" :minute-interval="5"
                                                hide-clear-button required></vue-timepicker>
                            </div>
                        </div>
                    </div>
                </div>

                <!--Save and Cancel Button-->
                <div class="row">
                    <div class="col-sm-12">
                        <ul class="list-inline">
                            <li>
                                <button class="btn btn-block btn-create-event btn-ignore" type="submit">SAVE EVENT
                                </button>
                            </li>
                            <li>
                                <button @click="cancel_button" class="btn btn-block btn-preview btn-ignore"
                                        type="button">
                                    CANCEL
                                </button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </form>
        <!--<simplert :useRadius="true"-->
        <!--:useIcon="true"-->
        <!--ref="simplert">-->
        <!--</simplert>-->
    </div>
</template>
<style>
    .event-details input {
        font-size: 14px;
    }

    /*-- overwriting forms css to adjust font size--*/
    .form-control {
        font-size: 14px;
    }

    .time-picker input.display-time {
        height: 40px !important;
        border: 1px solid #ccc;
        box-shadow: inset 0 1px 1px rgba(0, 0, 0, .075);
    }

    /*-- overwriting timepicker css to adjust font and width size--*/
    .timewrapper .time-picker input.display-time {
        border: 1px solid #d2d2d2;
        display: block;
        width: 28em;
        padding: 0.3em 0.5em;
        font-size: 14px;
    }

    li {
        font-size: 14px;
    }

    .time-picker .dropdown .hint {
        color: #a5a5a5;
        cursor: default;
        font-size: 14px !important;
    }

</style>
<style scoped>
    @import '../../../node_modules/bootstrap/dist/css/bootstrap.css';
    @import "../../../node_modules/bootstrap-vue/dist/bootstrap-vue.css";
    @import "../../../node_modules/pikaday/css/pikaday.css";
    @import "../../../node_modules/clockpicker/dist/bootstrap-clockpicker.css";
    @import '~vuejs-noty/dist/vuejs-noty.css';
</style>
<script type="text/babel">
    import FormCell from '../../../main/js/components/form-cell.vue'
    import Pikaday from 'pikaday'
    import VueTimepicker from 'vue2-timepicker'
    //    import Simplert from 'vue2-simplert'

    //    import Simplert from 'vue2-simplert-plugin'
    //    import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown'
    //    import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item'
    //    import bDropdownDivider from 'bootstrap-vue/es/components/dropdown/dropdown-divider'

    export default {
        name: 'EventForm',
        data() {
            return {
                event,
                csrf,
                user,
                start: '',
                end: '',
                start_time: {
                    hh: "09",
                    mm: "00",
                    a: "am"
                },
                end_time: {
                    hh: "10",
                    mm: "00",
                    a: "am"
                },
                timepicker: {
                    width: '100em !important',
                    height: '100%',
                },
                date_diff: '',
                start_date_picker: '',
                end_date_picker: '',
                hour_diff: 1,
                minute_diff: 0
            }
        },
        components: {FormCell, VueTimepicker},
        computed: {
            start_date: function () {
                if (this.start.length > 0) {
                    var start_date = this.start + ' ' + this.start_time.hh + ':' +
                        this.start_time.mm + ' ' + this.start_time.a.toUpperCase()
                    start_date = new Date(start_date + ' UTC')
                    start_date = start_date.toISOString()
                    this.event.start_date = start_date
                }
                return this.event.start_date
            },
            end_date: function () {
                if (this.end.length > 0) {
                    var end_date = this.end + ' ' + this.end_time.hh + ':' +
                        this.end_time.mm + ' ' + this.end_time.a.toUpperCase()
                    end_date = new Date(end_date + ' UTC')
                    end_date = end_date.toISOString()
                    this.event.end_date = end_date

                }
                return this.event.end_date
            }

        },
        created() {
            let start_date_value
            let end_date_value
            if (this.event.start_date != null) {
                start_date_value = new Date(this.event.start_date)
                let ampm = start_date_value.getHours() >= 12 ? 'pm' : 'am';
                let minutes = start_date_value.getMinutes() < 10 ? '0' + start_date_value.getMinutes() : start_date_value.getMinutes();
                let hours = start_date_value.getHours() % 12;
                hours = hours ? hours : 12
                this.start_time = {
                    hh: hours,
                    mm: minutes,
                    a: ampm
                }
            } else {
                this.start_time = {
                    hh: "09",
                    mm: "00",
                    a: "am"
                }
            }

            if (this.event.end_date != null) {
                end_date_value = new Date(this.event.start_date)
                let ampm = end_date_value.getHours() >= 12 ? 'pm' : 'am';
                let minutes = end_date_value.getMinutes() < 10 ? '0' + end_date_value.getMinutes() : end_date_value.getMinutes();
                let hours = end_date_value.getHours() % 12;
                hours = hours ? hours : 12
                this.end_time = {
                    hh: hours,
                    mm: minutes,
                    a: ampm
                }
            }

        },
        watch: {
            start_time: function (val) {
                let end_time_data = this.end_time
                if (this.hour_diff > 1 || this.minute_diff > 0) {
                    let add_diff_hour = parseInt(this.start_time.hh) + this.hour_diff
                    add_diff_hour = add_diff_hour.toString().length > 1 ? add_diff_hour.toString() : '0' + add_diff_hour.toString()
                    let add_min_diff = parseInt(this.start_time.mm) + this.minute_diff
                    add_min_diff = add_min_diff.toString().length > 1 ? add_min_diff.toString() : '0' + add_min_diff.toString()
                    this.end_time = {
                        hh: add_diff_hour,
                        mm: add_min_diff,
                        a: "pm"
                    }
                } else {
//                    this.end_time.hh = parseInt(this.start_time.hh) + 1
                    let add_hour = parseInt(this.start_time.hh) + 1
                    add_hour = add_hour.toString().length > 1 ? add_hour.toString() : '0' + add_hour.toString()
                    this.end_time = {
                        hh: add_hour,
                        mm: "00",
                        a: "pm"
                    }
                }

            },
            end_time: function (val) {
                let start_time_data = this.start_time
                this.hour_diff = parseInt(this.end_time.hh) - parseInt(start_time_data.hh)
                this.minute_diff = parseInt(this.end_time.mm) - parseInt(start_time_data.mm)
            }
        },
        methods: {
            cancel_button() {
                window.location.replace('/events/')
            },
            get_date_format(date) {
                let year = date.getFullYear()
                let month = (1 + date.getMonth()).toString()
                month = month.length > 1 ? month : '0' + month
                let day = date.getDate().toString()
                day = day.length > 1 ? day : '0' + day
                let return_date = month + '/' + day + '/' + year
                return return_date
            }
        },
        mounted() {
            const that = this
            let start_value = new Date()
            let end_value = new Date()

            if (this.event.start_date != null) {
                start_value = new Date(this.event.start_date)
                let year = start_value.getFullYear()
                let month = (1 + start_value.getMonth()).toString()
                month = month.length > 1 ? month : '0' + month
                let day = start_value.getDate().toString()
                day = day.length > 1 ? day : '0' + day
                this.start = month + '/' + day + '/' + year
//                this.start = start_value.toISOString()
            } else {
                let year = start_value.getFullYear()
                let month = (1 + start_value.getMonth()).toString()
                month = month.length > 1 ? month : '0' + month
                let day = start_value.getDate().toString()
                day = day.length > 1 ? day : '0' + day
                this.start = month + '/' + day + '/' + year
            }

            if (this.event.end_date != null) {
                end_value = new Date(this.event.end_date)
                let year = end_value.getFullYear()
                let month = (1 + end_value.getMonth()).toString()
                month = month.length > 1 ? month : '0' + month
                let day = end_value.getDate().toString()
                day = day.length > 1 ? day : '0' + day
                this.end = month + '/' + day + '/' + year
            } else {
                let year = end_value.getFullYear()
                let month = (1 + end_value.getMonth()).toString()
                month = month.length > 1 ? month : '0' + month
                let day = end_value.getDate().toString()
                day = day.length > 1 ? day : '0' + day
                this.end = month + '/' + day + '/' + year
            }

            this.start_date_picker = new Pikaday({
                field: document.getElementById('start_date'),
                format: 'MM/DD/YY',
                firstDay: 1,
                numberOfMonths: 1,
                mainCalendar: 'left',
                minDate: start_value,
                defaultDate: start_value,
                setDefaultDate: start_value,
                onSelect: function () {
                    that.start = this.getMoment().format('MM/DD/YY')
                    that.$nextTick(function () {
                        if (that.date_diff > 0) {
                            let result_date = new Date()
                            let start_new = new Date(that.start)
                            result_date.setDate(start_new.getDate() + that.date_diff)
                            let new_end = that.get_date_format(result_date)

                            //set new end
                            that.end_value = new_end
                            $('#end_date').val(that.end_value)
                            that.end_date_picker.setDate(that.end_value)
                            that.end = $('#end_date').val()
//                            that.end_value =
                        } else {
                            that.end_value = that.start
                            $('#end_date').val(that.end_value)
                            that.end_date_picker.setDate(that.end_value)
                            that.end = $('#end_date').val()
                            that.end_value = $('#end_date').val()
                        }

                    })
                }
            })

            this.end_date_picker = new Pikaday({
                field: document.getElementById('end_date'),
                format: 'MM/DD/YY',
                firstDay: 1,
                numberOfMonths: 1,
                mainCalendar: 'left',
                minDate: end_value,
                defaultDate: end_value,
                setDefaultDate: end_value,
                onSelect: function () {
                    let there = this
                    that.$nextTick(function () {
                        let start_date = $('#start_date').val()
                        if (that.start > that.end) {
                            // show modal here
                            $('#end_date').val(start_date)
                            that.end = $('#end_date').val()
                            that.end_date_picker.setDate(that.start)
                            that.$noty.error("End date should be later than start date")
                        } else {
                            that.end = there.getMoment().format('MM/DD/YY')
                            that.date_diff = new Date(that.end).getDate() - new Date(that.start).getDate()
                        }
                    })
                }
            })
        },
    }
</script>