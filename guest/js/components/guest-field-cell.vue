<template>
    <div class="row">
        <ul id="draggablePanelList" class="list-unstyled sortable_ul">
            <li class="panel" v-for="(field, index) in guest_fields">
                <input class="form-control" type="hidden" name="event_id" :value="event_id"/>
                <div :class="hidden_class(field.is_hidden)">
                    <div class="col-md-7 col-sm-7">
                        <input v-model="field.field_name" :placeholder="field.field_name"
                               type="text"
                               class="form-control"
                               :required="required"/>
                    </div>
                    <div class="col-sm-5">
                        <ul class="list-inline list-field-selection">
                            <li>
                                <label class="checkbox-inline">
                                    <input v-model="field.is_unique" type="checkbox">
                                    <a rel="tooltip" title="Unique - is used to identify fields
                            that cannot contain similar entry.">
                                        Unique</a>
                                </label>
                            </li>
                            <li>
                                <label class="checkbox-inline">
                                    <input type="checkbox" v-model="field.is_required"> <a rel="tooltip"
                                                                                           title="Required - is used to identify a fields that should not be empty.">
                                    Required</a>
                                </label>
                            </li>
                            <li>
                                <label class="checkbox-inline">
                                    <input type="checkbox" v-model="field.is_email">
                                    <a rel="tooltip" title="Email - is used to identify an email field.">Email </a>
                                </label>
                            </li>
                            <li class="delete-icon pull-right">
                                <a v-if="!default_fields.includes(field.field_name)"
                                   @click="delete_field(index, field.id)"><span class="icon-trash" data-toggle="tooltip"
                                                                                data-placement="top"
                                                                                title="Delete this custom field."></span></a>
                                <a @click="set_hidden(index, field.id, event_id, field.field_name, field.is_hidden)">
                                <span class="icon-eye" data-toggle="tooltip" data-placement="top"
                                      title="This will hide this field."></span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </li>
        </ul>

        <modal name="modal_delete" :height="200">
            <div class="modal-content">
                <div class="modal-header">
                    <h4>ARE YOU SURE YOU WANT TO DELETE?</h4>
                </div>
                <div class="modal-body" style="padding: 20px">
                    <center>
                        <ul class="list-inline ul-button">
                            <li>
                                <button class="btn btn-delete-yes " type="button" @click="emit_delete">YES</button>
                            </li>
                            <li>
                                <button class="btn btn-delete-no" type="button" @click="cancel_modal">CANCEL </button>
                            </li>
                        </ul>
                    </center>
                </div>
            </div>
        </modal>
    </div>
</template>
<style>
    @import '../../../node_modules/jquery-ui/themes/base/sortable.css'

    .modal-body {
        padding: 20px !important;
    }

    .v--modal-overlay {
        background: rgba(0, 0, 0, 0.5);
    }

</style>
<script type="text/babel">

    import sortable from '../../../node_modules/jquery-ui/ui/widgets/sortable'

    export default {
        name: 'field',
        props: {
            event_id: {
                type: Number,
                required: true
            },
            items: {
                type: Array,
                required: true
            },
            required: {
                type: Boolean
            }
        },
        data() {
            return {
                default_fields: ['First Name', 'Last Name', 'Company', 'Email Address', 'Phone Number', 'Designation', 'Title'],
                position: '',
                val: '',
                guest_fields: []
            }
        },
        created() {
            for (let item of this.items) {
                this.guest_fields.push(item)
            }
        },
        mounted() {
            var that = this
            let old_index = ''
            let new_index = ''
            $('.sortable_ul').sortable({
                start: function (event, ui) {
                    old_index = ui.item.index()
                },
                update: function (event, ui) {
                    new_index = ui.item.index()
                    let data_cut = that.items.splice(old_index, 1)[0]
                    that.items.splice(new_index, 0, data_cut)
                }
            })
        },
        watch: {
            items: function (val) {
                this.items = val
//                this.guest_fields = val
                this.$emit('item_update', val)
            }
        },
        methods: {
            hidden_class(is_hidden) {
                if (is_hidden) {
                    return 'panel-body panel-disabled'
                } else {
                    return 'panel-body'
                }
            },
            emit_delete() {
                this.$emit('delete_item', this.position, this.val)
                this.$modal.hide('modal_delete')
            },
            cancel_modal() {
                this.$modal.hide('modal_delete')
            },
            delete_field(position, val) {
                this.position = position
                this.val = val
                this.$modal.show('modal_delete')
            },
            set_hidden(position, id, event_id, field_name, hidden) {
                hidden = !hidden
                this.$emit('set_hidden', position, id, event_id, field_name, hidden)
            }
        }
    }
</script>