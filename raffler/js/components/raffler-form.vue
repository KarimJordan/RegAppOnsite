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
                        <center><h4>E-RAFFLER</h4></center>
                    </nav>
                </div>
            </div>
        </div>

        <div class="container">
            <form method="post" action="" role="form">
                <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                <input type="hidden" name="num_of_draws_done" v-model="raffle_data.num_of_draws_done"/>
                <input type="hidden" name="event" :value="event_id"/>
                <div class="event-details container-box">
                    <h3>Setup new draw</h3>
                    <div class="row">
                        <div class="col-sm-6">
                            <label>RAFFLE TITLE</label>
                            <form-cell :type="input" name="title" v-model="raffle_data.title" :required="true"
                                       :autofocus="true">
                            </form-cell>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-6">
                            <label>NUMBER OF DRAWS</label>
                            <form-cell :type="input" name="num_of_draws" v-model="raffle_data.num_of_draws"
                                       :required="true" :autofocus="true">
                            </form-cell>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-3">
                            <label>DRAW DURATION</label>
                            <form-cell :type="input" name="draw_duration" v-model="raffle_data.draw_duration"
                                       :required="true" :autofocus="true" placeholder="sec">
                            </form-cell>
                        </div>
                        <div class="col-sm-3">
                            <label>ITEM DURATION</label>
                            <form-cell :type="input" name="item_duration" v-model="raffle_data.item_duration"
                                       :required="true" :autofocus="true" placeholder="ms">
                            </form-cell>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-6">
                            <label>PRIZE LABEL</label>
                            <form-cell :type="input" name="label" v-model="raffle_data.label"
                                       :required="true" :autofocus="true">
                            </form-cell>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-6">
                            <label>PRIZE Image</label>
                            <p>Prize Image Height must be atleast 300px.</p>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-6">
                            <div class="fileUpload upload-btn">
                                <center><span class="icon icon-image-upload"></span></center>
                                <form enctype="multipart/form-data" method="post">
                                    <input @change="upload_prize($event.target.files)" type="file" class="upload"/>
                                </form>
                            </div>
                            <input type="hidden" v-model="prize_image_value" name="prize_image"/>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-6">
                            <img :src="prize_image_value" height="300" width="524"/>
                        </div>
                    </div>

                    <hr>

                    <div class="row">
                        <div class="col-sm-6">
                            <label>Background Image</label>
                            <p>Background Image must be atleast 1920px in width and 1080px in height.</p>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-6">
                            <div class="fileUpload upload-btn">
                                <center><span class="icon icon-image-upload"></span></center>
                                <form enctype="multipart/form-data" method="post">
                                    <input @change="upload_background($event.target.files)" type="file" class="upload"/>
                                </form>
                                <input type="hidden" v-model="background_image_value" name="background_image"/>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col-sm-6">
                            <img :src="background_image_value" height="300" width="524"/>
                        </div>
                    </div>

                    <hr>
                    <div class="row">
                        <div class="col-sm-12" style="margin-top: 30px;">
                            <label>SELECTION FILTER</label>
                            <div class="table">
                                <table class="table">
                                    <raffler-selection-filter
                                            @remove="remove_filter"
                                            :selection_filter="selection_filter"
                                            :guest_fields="guest_fields">

                                    </raffler-selection-filter>
                                    <tfoot>
                                    <tr>
                                        <th colspan="5">
                                            <button @click="add_selection_filter" id="btnAdd" type="button"
                                                    class="btn bg-main" data-toggle="tooltip"
                                                    data-original-title="Add more controls"><i
                                                    class="glyphicon glyphicon-plus-sign"></i>&nbsp; Add New&nbsp;
                                            </button>
                                        </th>
                                    </tr>
                                    </tfoot>
                                </table>
                            </div>
                        </div>
                    </div>
                    <input type="hidden" name="conditions" :value="JSON.stringify(selection_filter)"/>
                    <center>
                        <button class="btn btn-block btn-create-event btn-ignore" type="submit">SAVE</button>
                    </center>
                </div>
            </form>
        </div>
    </div>
</template>
<style>

</style>
<script type="text/babel">

    import axios from 'axios'
    //    import audioplayer from 'audio-player'
    import audioplayer from '../external/audio-player'
    import RafflerSelectionFilter from './raffler-selection-filter.vue'
    import FormCell from '../../../main/js/components/form-cell.vue'

    export default {

        name: 'RafflerForm',
        data() {
            return {
                raffle_data,
                event_id,
                guest_fields,
                condi_data,
                selected_field: '',
                selected_info: '',
                guest_infos: [],
                selection_filter: [],
                prize_image_value: '',
                background_image_value: '',
                csrf,
                selection_data: {
                    selected_filter: 'Include',
                    selected_field: 'All',
                    selected_value: 'All',
                    field_values: [],
                },
                conditions_data: [],
            }
        },
        created() {
            if (this.raffle_data.prize_image != '') {
                this.prize_image_value = this.raffle_data.prize_image
            }
            if (this.raffle_data.background_image != '') {
                this.background_image_value = this.raffle_data.background_image
            }
//              for (let field of this.guest_fields){
//                  this.selection_data.selected_field.push(field)
//              }
            if (this.condi_data != '') {
                this.selection_filter = this.condi_data
            } else {
                this.selection_filter.push(this.selection_data)
            }
        },
        components: {RafflerSelectionFilter, FormCell},
        computed: {
            conditions: function () {
                return this.selection_filter
            }
        },
        watch: {
            selected_field: function (val) {
                this.selected_field = val
                this.get_field_values()
            },
        },
        methods: {
            remove_filter(index) {
                this.selection_filter.splice(index, 1)
            },
            add_selection_filter() {
                let data = {
                    selected_filter: 'Include',
                    selected_field: 'All',
                    selected_value: 'All',
                    field_values: [],
                }
                this.selection_filter.push(data)
            },
            upload_background(file) {
                let that = this
                let fileData = file[0]
                let fileReader = new FileReader()
                fileReader.readAsDataURL(fileData)
                fileReader.onload = function (e) {
                    let outputFile = e.target.result
                    that.background_image_value = outputFile
                }
            },
            upload_prize(file) {
                let that = this
                let fileData = file[0]
                let fileReader = new FileReader()
                fileReader.readAsDataURL(fileData)
                fileReader.onload = function (e) {
                    let outputFile = e.target.result
                    that.prize_image_value = outputFile
                }
            },
            save() {

            },
            get_field_values() {
                let params = {
                    selected_field: this.selected_field
                }
                let url = 'api/field_value_list/'
                params = {params: params}
                axios.get(url, params).then((response) => {
                    this.guest_infos = response.data.guest_infos
                })
            }
        }
    }
</script>