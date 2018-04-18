<template>
    <div>
        <!--<div class="event-details container-box-multiple" v-for="duplicate in duplicates">-->
            <!--<div class="row-margin">-->
            <!--</div>-->
        <!--</div>-->

        <div  v-for="duplicate in duplicates">
            <div class="table-scroll  no-margin no-padding" id="table-scroll">
                <div class="table-wrap">
                <table class="main-table duplicate-td" id="table" data-show-columns="false" data-search="false" data-show-toggle="false" data-pagination="false" data-resizable="true">
                    <thead>
                    <tr>
                        <th class="fixed-side">Actions</th>
                        <th v-for="field in fields" scope="col" :data-field="field.field_name.replace(' ', '').toLowerCase()">{{field.field_name}}</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(dup, index) in duplicate">
                        <td class="fixed-side">
                            <div v-if="duplicate_info[dup][0].edit">
                                <button type="button" @click="save_info(dup)"
                                        class="btn-duplicate-save">
                                    Save
                                </button>
                            </div>
                            <div v-if="!duplicate_info[dup][0].edit">
                                <a @click="edit(dup)">
                                    <span class="icon icon-pencil edit-icn"></span>
                                </a>
                                <a @click="delete_dup(dup, duplicate, index)"><span
                                        class="icon icon-trash remove-icn"></span></a>
                            </div>
                        </td>
                        <td v-for="item in duplicate_info[dup]">
                            <div v-if="item.edit">
                                <input type="text" v-model="item.value"/>
                            </div>
                            <div v-else>
                                {{item.value}}
                            </div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
            </div>

            <div class="col-sm-12 duplicate-buttons">
                <center>
                    <ul class="list-inline ul-button">
                        <!--<li>-->
                        <!--<button class="btn btn-block btn-ignore btn-ignore-new" type="button">IGNORE CONFLICTS-->
                        <!--</button>-->
                        <!--</li>-->
                        <li>
                            <a :href="'/events/' + event_id + '/duplicates_list/'">
                                <button class="btn btn-block btn-resolve">SAVE</button>
                            </a>
                        </li>
                        <li>
                            <a :href="'/events/'+ event_id + '/'">
                                <button class="btn btn-block btn-ignore-new" type="button">Ignore All</button>
                            </a>
                        </li>
                    </ul>
                </center>
            </div>
        </div>
    </div>
</template>
<style scoped>
    td button {
        font-size: 14px;
    }
    td {
        font-size: 14px;
    }


</style>
<script type="text/babel">

    import axios from 'axios'

    export default {
        name: 'EventDuplicateCell',
        props: {
            csrf: {
                type: String,
            },
            event_id: {
                type: Number,
            },
            fields: {
                type: Array,
                required: true
            },
            duplicates: {
                type: Array,
                required: true
            },
            duplicate_info: {
                type: Object,
                required: true
            }
        },
        methods: {
            edit(dup) {
                for (let i = 0; i < this.duplicate_info[dup].length; i++) {
                    this.duplicate_info[dup][i].edit = !this.duplicate_info[dup][i].edit
                }
            },
            save_info(dup) {
                for (let i = 0; i < this.duplicate_info[dup].length; i++) {
                    this.duplicate_info[dup][i].edit = !this.duplicate_info[dup][i].edit
                    let data = {
                        'id': this.duplicate_info[dup][i].id,
                        'value': this.duplicate_info[dup][i].value,
                        'key': this.duplicate_info[dup][i].key,
                        'event_id': this.duplicate_info[dup][i].event_id,
                        'guest_id': this.duplicate_info[dup][i].guest_id,
                        'guest_info_field_id': this.duplicate_info[dup][i].guest_info_field_id
                    }
                    const request = {
                        method: 'post',
                        url: '/guest/info/' + this.event_id + '/',
                        data: data,
                        headers: {'X-CSRFToken': this.csrf}
                    }

                    axios(request)
                        .then((response) => {
                            //console.log(response)
                            //window.location.replace(redirect);
                        })
                        .catch((error) => {
                            console.log(error)
                        })
                }
            },
            delete_dup(dup, duplicate, index) {
                this.duplicates.splice(index, 1)

                let url = '/guests/' + this.event_id + '/delete_info/'
                let data = {
                    'guest_id': this.duplicate_info[dup][0].guest_id,
                }
                const request = {
                    method: 'post',
                    url: '/guest/delete/' + this.event_id + '/',
                    data: data,
                    headers: {'X-CSRFToken': this.csrf}
                }

                axios(request)
                    .then((response) => {
                        //console.log(response)
                        //window.location.replace(redirect);
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            }
        }
    }
</script>