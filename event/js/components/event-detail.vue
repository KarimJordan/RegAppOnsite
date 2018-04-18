<template>
    <div>
        <!--<modal :title="modal.title" :visible.sync="modal.visible" :bg-click="false" :verify="true">-->
        <!--<p class="control">-->
        <!--<label class="label">Name:</label>-->
        <!--<input class="input" type="text" v-model="modal.text" placeholder="Your name">-->
        <!--</p>-->
        <!--</modal>-->


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

        <!--<sweet-modal @close="closeModal" class="col-12" ref="entry">KJSAHKSHKAj</sweet-modal>-->
        <div class="sub-header" role="banner">
            <div class="container">
                <div class="sub-head-nav">
                    <center><h4>EVENT PAGE</h4></center>
                </div>
            </div>
        </div>
        <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
        <div class="container">
            <div class="container-box">
                <!--Guest Header-->
                <div class="row">

                    <!--Number of Guests-->
                    <div class="col-sm-3">
                        <div class="box-number">
                            <h1>{{ event.no_of_guest }}</h1>
                            <p v-if="parseInt(event.no_of_guest) > 1">GUESTS</p>
                            <p v-if="parseInt(event.no_of_guest) <= 1">GUEST</p>
                        </div>
                    </div>

                    <!--Event Details-->
                    <div class="col-sm-9">
                        <div class="box-det">
                            <span class="head-t">{{ event.name }}</span>

                            <form action="" method="POST" class="form-inline pull-right">
                                <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                <input type="hidden" name="_method" value="put">
                                <button type="submit" style="background-color: Transparent;
                                                            border: none;
                                                            cursor:pointer;
                                                            overflow: hidden;
                                                            outline:none;">
                                    <a @click="update_event" href="" class="Right" style="float: right;">
                                    <span class="icon icon-pencil edit-icn" alt="Edit Inforamtion">
                                    </span>
                                    </a>
                                </button>
                            </form>

                            <div class="form-group details">
                                <label class="col-sm-3 col-form-label">Starts at</label>
                                <div class="col-sm-9">
                                    <p>{{ event.start_date }}</p>
                                </div>
                                <br>
                                <label class="col-sm-3 col-form-label">Ends at</label>
                                <div class="col-sm-9">
                                    <p>{{ event.end_date }}</p>
                                </div>
                                <br>
                                <label class="col-sm-3 col-form-label">Venue</label>
                                <div class="col-sm-9">
                                    <p>{{ event.venue }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <ul class="list-inline col-sm-12 btn-box">
                        <li>
                            <button @click="show_layout_list" type="button" class="btn-send-invite"><span
                                    class="icon icon-irs-icn"></span>IRS EDITOR
                            </button>
                            <!--<form class="btn-send-invite" id="irs_form" action="/layouts/" method="post">-->
                            <!--<input type="hidden" name="csrfmiddlewaretoken" :value="csrf">-->
                            <!--<a v-on:click="createLayout">-->
                            <!--<span class="icon icon-irs-icn"></span>-->
                            <!--IRS EDITOR-->
                            <!--</a>-->
                            <!--</form>-->
                        </li>
                        <li>
                            <button @click="raffler" type="button" class="btn-send-invite"><span
                                    class="icon icon-reffler-icn"></span>E-RAFFLER
                            </button>
                        </li>
                    </ul>

                </div>

                <!--Guest Management-->
                <div class="row">
                    <div class="col-sm-12">
                        <div class="form-group guest-list">
                            <!--Upload and Download Excel-->
                            <ul class="list-inline">
                                <li class="pull-right">
                                    <span class="icon download-excel icon-image-download">
                                    </span>
                                    <a id="download-btn"
                                       :href="'/events/' + event.id + '/download_guest/'"
                                       target="_blank"
                                       class="download-excel">Download Excel</a>
                                </li>
                                <li class="pull-right">
                                    <!--<form id="upload_excel" action="/events/upload/" enctype="multipart/form-data" method="post">-->
                                    <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                    <span class="icon icon-image-upload"></span><a
                                        @click="uploadExcel">Upload Excel</a>
                                    <!--</form>-->
                                </li>
                            </ul>
                            <h3 col-sm-3>Guest List</h3>
                        </div>
                    </div>
                </div>

                <!--Search-->
                <div class="row">
                    <div class="col-sm-12">
                        <ul class="list-inline">
                            <li>
                                <form method="post" :action="'/guests/fields/' + event.id + '/'">
                                    <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                    <button type="submit" class="btn-manage-g"><span
                                            class="icon icon-person"></span>Manage Guest Fields
                                    </button>
                                </form>
                            </li>
                            <li>
                                <form method="post" action="/guests/">
                                    <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                    <button type="submit" class="btn-manage-g"><span
                                            class="icon icon-person"></span>Add Guests
                                    </button>
                                </form>
                            </li>
                            <li v-if="duplicates_list.length > 0">
                                <a :href="get_duplicates_link(duplicates_list.length)"
                                   :class="get_dup_indicator(duplicates_list.length)">
                                    <button type="button" class="btn-manage-g" id="dup-btn"><span
                                            class="icon icon-person"
                                    ></span>{{get_dups(duplicates_list.length)}} Duplicate Entries
                                    </button>
                                </a>
                            </li>
                            <li class="pull-right">
                                <form action="" class="search-form">
                                    <div class="form-group has-feedback">
                                        <label class="sr-only">Search</label>
                                        <input v-model="search" type="text" class="form-control"
                                               placeholder="search">
                                        <span class="glyphicon glyphicon-search form-control-feedback"></span>
                                    </div>
                                </form>
                            </li>
                        </ul>
                        <hr>
                    </div>
                </div>

                <!--  <div class="row">
                     <div class="form-group">
                         <select class="form-control" v-model="action">
                             <option value="Action">Action</option>
                             <option value="Delete">Delete</option>
                         </select>
                     </div>
                 </div> -->

                <!--Tabs-->
                <div class="row">
                    <!--Guest Lists-->
                    <div class="col-sm-12">
                        <div class="bs-example bs-example-tabs" role="tabpanel" data-example-id="togglable-tabs">
                            <div class="form-group action-drop-btn">
                                <select class="form-control" id="sel1" v-model="action">
                                    <option :value="'none'">Action</option>
                                    <option :value="'delete'">Delete</option>
                                </select>
                            </div>
                            <ul id="myTab" class="nav nav-tabs nav-tabs-responsive" role="tablist">
                                <li @click="list_guest('All')" :class="status_tab('All')" role="presentation">
                                    <a role="tab"
                                       aria-controls="home" aria-expanded="true">
                                        <span class="text">All </span>
                                    </a>
                                </li>

                                <li @click="list_guest('Walkin')" :class="status_tab('Walkin')" role="presentation" i>
                                    <a role="tab"
                                       aria-controls="home" aria-expanded="true">
                                        <span class="text">Walkin </span>
                                    </a>
                                </li>

                                <li @click="list_guest('Pre Registered')" :class="status_tab('Pre Registered')"
                                    role="presentation" i>
                                    <a role="tab"
                                       aria-controls="home" aria-expanded="true">
                                        <span class="text">Pre Registered </span>
                                    </a>
                                </li>

                                <li @click="list_guest('Registered')" :class="status_tab('Registered')"
                                    role="presentation" i>
                                    <a role="tab"
                                       aria-controls="home" aria-expanded="true">
                                        <span class="text">Registered </span>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>


                <paginate name="guest_list_info"
                          :list="guest_list_info"
                          :per="limit_page">
                    <!--Data Table-->
                    <div class="table-scroll no-margin no-padding" id="table-scroll">
                        <div class="table-wrap">
                            <table class="main-table checkbox-table" id="table" data-show-columns="false"
                                   data-search="false" data-show-toggle="false" data-pagination="false"
                                   data-resizable="true">
                                <thead>
                                <tr>
                                    <th class="fixed-side"><input type="checkbox">Actions</th>
                                    <th scope="col" :data-field="field.field_name.replace(' ', '').toLowerCase()"
                                        v-for="field in guest_fields">
                                        {{field.field_name}}
                                    </th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr v-for="(guest, index) in paginated('guest_list_info')">
                                    <td class="fixed-side">
                                        <input v-if="!guest.edit" type="checkbox"
                                               @click="add_delete(index, !guest.checked)" v-model="guest.checked">
                                        <a v-if="!guest.edit" @click="edit_info(index)"><span
                                                class="i    con icon-pencil edit-icn"
                                                style="font-size: 14px"></span></a>
                                        <button type="button" v-if="guest.edit" @click="save_info(index, guest.id)"
                                                class="btn-duplicate-save">
                                            Save
                                        </button>
                                    </td>
                                    <td v-if="guest.event_id == info.event_id && guest.id == info.guest_id"
                                        v-for="info in guest_infos">
                                        <div v-if="guest.edit">
                                            <input type="text" v-model="info.value"/>
                                        </div>
                                        <div v-else>
                                            {{info.value}}
                                        </div>

                                    </td>
                                </tr>
                                </tbody>

                            </table>
                        </div>
                    </div>
                </paginate>
                <ul class="list-inline">
                    <li class="pull-left" style="padding-top: 20px;">
                        <select class="form-control" v-model="limit_page">
                            <option :value="10">10 / Page</option>
                            <option :value="30">30 / Page</option>
                            <option :value="50">50 / Page</option>
                        </select>

                    </li>
                    <li>
                        <paginate-links for="guest_list_info"
                                        :show-step-links="true" :async="true"></paginate-links>
                    </li>

                </ul>
            </div>
        </div>

        <modal style="left:0% !important;" name="upload_excel">
            <div class="modal-content">
                <div class="modal-header">
                    <button @click="hide" type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>
                </div>
                <div class="modal-body" style="text-align: center;">
                    <h4 class="modal-title" id="myModalLabel">UPLOAD EXCEL GUEST</h4>
                    <form :action="'/events/' + event.id + '/upload_excel/'"
                          enctype="multipart/form-data"
                          method="post">
                        <center>
                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                            <input style="min-width: 300px;" name="file" type="file"
                                   placeholder='Choose a file...'/>
                        </center>
                        <center>
                            <button class="btn btn-manage-g" type="submit">UPLOAD</button>
                        </center>
                    </form>
                </div>
            </div>
        </modal>


        <modal name="layout_lists" :height="560">
            <div class="modal-content">
                <!--<button @click="hide" type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>-->
                <div class="modal-header">
                    <h4 class="modal-title">Select Saved Layouts</h4>
                </div>
                <div class="modal-body">
                    <center>
                        <form id="irs_form" action="/layouts/" method="post">
                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                            <button type="submit" class="btn-default-layout"><span
                                    class="icon icon-irs-icn"></span>Default Layout
                            </button>
                            <br>
                        </form>
                    </center>
                    <table v-if="layouts.length > 0" class="table table-bordered table-layout table-modal-button">
                        <thead>
                        <tr>
                            <th>Layout Name</th>
                            <th>Date Created</th>
                            <th>Date Modified</th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="layout in layouts">
                            <td>
                                {{layout.layout_name}}
                                <!--<form :id="'layout_form-' + layout.id" :action="/layouts/ + layout.id + '/'">-->
                                <!--<input type="hidden" name="csrfmiddlewaretoken" :value="csrf">-->
                                <!--<input type="hidden" name="_method" value="put">-->
                                <!--<a @click="update_layout(layout.id)">-->
                                <!--{{layout.layout_name}}-->
                                <!--</a>-->
                                <!--</form>-->
                            </td>
                            <td>{{layout.created}}</td>
                            <td>{{layout.modified}}</td>
                            <td>
                                <ul class="list-inline pull-right">
                                    <li>
                                        <form :id="'layout_form-' + layout.id" :action="/layouts/ + layout.id + '/'">
                                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                            <input type="hidden" name="_method" value="put">
                                            <a @click="update_layout(layout.id)">
                                                <span class="icon icon-pencil edit-layout-icn"></span>
                                            </a>
                                        </form>
                                    </li>
                                    <li>

                                        <form :action="/layouts/ + layout.id + '/'" method="POST">
                                            <input type="hidden" name="csrfmiddlewaretoken" :value="csrf">
                                            <button class="event-delete-btn" name="_method" value="delete"
                                                    type="submit">
                                                <span class="icon icon-trash"></span>
                                            </button>
                                        </form>
                                        <!--<a href="#"><span class="icon icon-trash delete-layout-icn"></span></a>-->
                                    </li>
                                </ul>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    <div v-else style="text-align: center">
                        <h4 class="modal-title">
                            Event has no layouts yet created.
                        </h4>
                    </div>
                </div>
            </div>
        </modal>
    </div>
</template>
<style scoped>
    .table-modal-button {
        padding-top: 20px !important;
    }

    .modal-body {
        padding-top: 5% !important;
    }

    .v--modal-overlay {
        position: fixed;
        box-sizing: border-box;
        left: 0px;
        top: 0px;
        width: 100%;
        height: 100vh;
        z-index: 99999;
        opacity: 1;
        background: rgba(0, 0, 0, 0.5);
    }
</style>


<script type="text/babel">

    import axios from 'axios'
    import $ from 'jquery'
    import Paginate from "vue-paginate/src/components/Paginate";

    export default {
        components: {Paginate},
        name: 'EventDetail',
        data() {
            return {
                action: 'Action',
                paginate: ['guest_list_info'],
                layouts: layouts,
                event: event,
                guest_list: guest_list,
                guest_list_info: [],
                guest_fields: guest_fields,
                guest_infos: guest_infos,
                guest_info_init: [],
                csrf,
                duplicates_list,
                logout_url,
                search: '',
                showModal: false,
                activebar: 'All',
                to_be_deleted: [],
                limit_page: 10,
                action: ''
            }
        },
        created() {
            for (let g of this.guest_list) {
                let data = {
                    type: g.type,
                    code: g.code,
                    id: g.id,
                    event_id: g.event_id,
                    edit: false
                }
                this.guest_list_info.push(data)
            }
            for (let info of this.guest_infos) {
                let data = {
                    id: info.id,
                    event_id: info.event_id,
                    guest_id: info.guest_id,
                    guest_info_field_id: info.guest_info_field_id,
                    key: info.key,
                    value: info.value
                }
                this.guest_info_init.push(data)
            }
        },
        watch: {
            action: function (val) {
                if (val == 'delete') {
                    // call delete function

                }
            },
            search: function (val) {
                this.get_guest_list()
            },
        },
        methods: {
            add_delete(index, guest_checked) {
                if (guest_checked) {
                    this.to_be_deleted.push(this.guest_list_info[index])
                } else {
                    let index = 0
                    for (let i = 0; i < this.to_be_deleted.length; i++) {
                        console.log(this.to_be_deleted[i].id)
                        console.log(this.guest_list_info[index].id)
//                        if (this.to_be_deleted[i].id == this.guest_list_info[index].id) {
//                            index = i
//                        }
                    }

                    console.log(index)
                }
                console.log(this.to_be_deleted)
            },
            get_duplicates_link(length) {
                if (length > 0) {
                    return '/events/' + this.event.id + '/duplicates_list/'
                } else {
                    return ''
                }
            },
            get_dups(length) {
                if (length > 0) {
                    return '(' + length + ')'
                } else {
                    return ''
                }
            },
            get_dup_indicator(length) {
                if (length > 0) {
                    return 'duplicate-on'
                } else {
                    return ''
                }
            },
            save_info(index) {
                this.guest_list_info[index].edit = false

                let a = this.guest_info_init
                let b = this.guest_infos
                let onlyInFirst = function (equal, a, b) {
                    return a.filter(function (current) {
                        return b.filter(equal(current)).length == 0
                    });
                }
                let onlyInFirstMyObject = onlyInFirst.bind(0, function equal(a) {
                    return function (b) {
                        return a.value == b.value &&
                            a.display == b.display
                    }
                });
                let result = onlyInFirstMyObject(b, a)
                for (const data of result) {
                    const request = {
                        method: 'post',
                        url: '/guest/info/' + this.event.id + '/',
                        data: data,
                        headers: {'X-CSRFToken': this.csrf}
                    }

                    axios(request)
                        .then((response) => {
                            console.log(response)
                            //window.location.replace(redirect);
                        })
                        .catch((error) => {
                            console.log(error)
                        })
                }
            },
            edit_info(index) {
                this.guest_list_info[index].edit = true
            },
            get_guest_list() {
                let params = {
                    search: this.search
                }
                let url = 'api/guest_events/'
                params = {params: params}
                axios.get(url, params).then((response) => {
                    this.guest_list = response.data.guest_list
                    this.guest_infos = response.data.guest_infos
                    this.guest_list_info = response.data.guest_list
                })
            },
            status_tab(tabname) {
                if (this.activebar == tabname) {
                    return 'status-tab active'
                } else {
                    return 'status-tab'
                }
            },
            list_guest(tabname) {
                this.activebar = tabname
                let params = {
                    type: tabname,
                    search: this.search
                }
                let url = 'api/guest_events/'
                params = {params: params}
                axios.get(url, params).then((response) => {
                    this.guest_list = response.data.guest_list
                    this.guest_infos = response.data.guest_infos
                    this.guest_list_info = response.data.guest_list
                })
            },
            update_event() {
                let event_update = document.getElementById('event_update')
                event_update.submit()
            },
            update_layout(id) {
                let update_form = document.getElementById('layout_form-' + id)
                update_form.setAttribute("method", "post")
                update_form.submit()
            },
            createLayout() {
                let irs_form = document.getElementById('irs_form')
                irs_form.submit()
            },
            show_layout_list() {
                this.$modal.show('layout_lists')
            },
            raffler() {
                window.location.replace('/rafflers/')
            },
            uploadExcel() {
                this.$modal.show('upload_excel')
            },
            hide() {
                this.$modal.hide('upload_excel')
            }
        }
    }
</script>