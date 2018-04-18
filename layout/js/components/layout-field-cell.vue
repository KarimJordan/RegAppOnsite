<template>
    <div>
        <!--<div v-for="(data, index) in style_data_list">-->
            <!--{{style_data_list[index].field_type}}-->
        <!--</div>-->
        <table :style="ipadForm">
            <tbody id="fields">
            <tr v-for="(item, index) in items_list">
                <div @mouseover="show_input('show')" @mouseout="show_input('hide')"
                     v-if="item.field_name == 'Spacer Field'">
                    <ul :style="show_input_display" class="list-inline">
                        <li @click="remove(index, item)" class="no-padding no-margin"><span
                                class="icon icon-circle-with-cross"
                                style="font-size: 12px"></span></li>
                        <li class="no-padding no-margin"><span class="fa fa-hand-paper-o"
                                                               style="font-size: 12px"></span></li>
                    </ul>
                    <input @click="set_selected(item.field_name, index)" placeholder="Spacer"
                           style="visibility:hidden; display: block; margin: 0
                    !important; border-color: #000; border-radius:5px;
                    color: #000; background: rgba(255, 255, 255, 1);">
                </div>

                <div @mouseover="show_input('show')" @mouseout="show_input('hide')"
                     v-if="style_list[index].field_type == 'Input Box' &&
                style_list[index].input_text_type == 'As Placeholder' && item.field_name != 'Spacer Field'">
                    <ul :style="show_input_display" class="list-inline">
                        <li @click="remove(index, item)" class="no-padding no-margin"><span
                                class="icon icon-circle-with-cross"
                                style="font-size: 12px"></span></li>
                        <li class="no-padding no-margin"><span class="fa fa-hand-paper-o"
                                                               style="font-size: 12px"></span></li>
                    </ul>
                    <input @click="set_selected(item.field_name, index)" :style="style_list[index]"
                           :placeholder="item.field_name"/>
                </div>

                <div v-if="style_list[index].field_type == 'Input Box' &&
                style_list[index].input_text_type == 'As Label' && item.field_name != 'Spacer Field'">
                    <ul :style="show_input_display" class="list-inline">
                        <li @click="remove(index, item)" class="no-padding no-margin"><span
                                class="icon icon-circle-with-cross"
                                style="font-size: 12px"></span></li>
                        <li class="no-padding no-margin"><span class="fa fa-hand-paper-o"
                                                               style="font-size: 12px"></span></li>
                    </ul>
                    <label :style="style_list[index].label_style">{{item.field_name}}
                    </label>
                    <div class="field-element">
                        <div class="field-element">
                            <input @click="set_selected(item.field_name, index)" :style="style_list[index]"
                                   type="text" :value="item.field_name" readonly>
                        </div>
                    </div>
                </div>

                <div @click="set_selected(item.field_name, index)"
                     v-if="style_list[index].field_type == 'Dropdown' && item.field_name != 'Spacer Field'">
                    <ul :style="show_input_display" class="list-inline">
                        <li @click="remove(index, item)" class="no-padding no-margin"><span
                                class="icon icon-circle-with-cross"
                                style="font-size: 12px"></span></li>
                        <li class="no-padding no-margin"><span class="fa fa-hand-paper-o"
                                                               style="font-size: 12px"></span></li>
                    </ul>
                    <select :style="style_list[index]">
                        <option v-for="value in style_list[index].dropdown_values" :values="value">{{value}}
                        </option>
                    </select>
                </div>

                <div @click="set_selected(item.field_name, index)"
                     v-if="style_list[index].field_type == 'Checkbox' && item.field_name != 'Spacer Field'">
                    <ul :style="show_input_display" class="list-inline">
                        <li @click="remove(index, item)" class="no-padding no-margin"><span
                                class="icon icon-circle-with-cross"
                                style="font-size: 12px"></span></li>
                        <li class="no-padding no-margin"><span class="fa fa-hand-paper-o"
                                                               style="font-size: 12px"></span></li>
                    </ul>
                    <label :style="style_list[index].label_style">{{item.field_name}}</label>
                    <div v-for="value in style_list[index].dropdown_values">
                        <div class="field-element">
                            <div class="checkbox">
                                <input type="checkbox">
                                <label :style="style_list[index].list_style">{{value}}</label>
                            </div>
                        </div>
                    </div>
                </div>

                <div @click="set_selected(item.field_name, index)"
                     v-if="style_list[index].field_type == 'Radio Button' && item.field_name != 'Spacer Field'">
                    <ul :style="show_input_display" class="list-inline">
                        <li @click="remove(index, item)" class="no-padding no-margin"><span
                                class="icon icon-circle-with-cross"
                                style="font-size: 12px"></span></li>
                        <li class="no-padding no-margin"><span class="fa fa-hand-paper-o"
                                                               style="font-size: 12px"></span></li>
                    </ul>
                    <label :style="style_list[index].label_style">{{item.field_name}}</label>
                    <div v-for="value in style_list[index].dropdown_values">
                        <div class="field-element">
                            <div class="field-element">
                                <input type="radio">
                                <label :style="style_list[index].list_style">{{value}}</label>
                            </div>
                        </div>
                    </div>
                </div>
            </tr>
            </tbody>
        </table>
    </div>
</template>
<style>
    @import '../../../node_modules/jquery-ui/themes/base/sortable.css';
</style>
<script type="text/babel">

    import sortable from '../../../node_modules/jquery-ui/ui/widgets/sortable'

    export default {
        name: 'LayoutFieldCell',
        created() {
            for (let item of this.items) {
                this.items_list.push(item)
            }

            for (let style of this.style_data_list) {
                this.style_list.push(style)
            }

            for (let i = 0; i < this.items.length; i++) {
                let with_placeholder = false
                if (this.style_data_list[i].input_text_type == 'As Placeholder') {
                    with_placeholder = true
                }
                let data = {
                    guest_info_field_id: this.items[i].id,
                    type: this.style_data_list[i].field_type,
                    height: '',
                    width: this.style_data_list[i].width.replace("px", ""),
                    page_num: '1',
                    field_name: this.items[i].field_name,
                    order: i.toString(),
                    with_placeholder: with_placeholder,
                    font_family: this.style_data_list[i].fontFamily,
                    font_color: this.style_data_list[i].color,
                    font_size: this.style_data_list[i].fontSize.replace("px", ""),
                    background_color: this.style_data_list[i].background,
                    opacity: this.style_data_list[i].field_opacity,
                    border_color: this.style_data_list[i].borderColor,
                    label_color: this.style_data_list[i].label_style.color,
                    label_size: this.style_data_list[i].label_style.fontSize.replace("px", ""),
                    label_font_family: this.style_data_list[i].label_style.fontFamily,
                    list_font_color: this.style_data_list[i].list_style.color,
                    list_font_family: this.style_data_list[i].list_style.fontFamily,
                    list_font_size: this.style_data_list[i].list_style.fontSize.replace("px", ""),
                    field_values: this.style_data_list[i].dropdown_values,
                }
                this.layout_fields.push(data)
            }
            this.$emit('layout_fields', this.layout_fields)
        },
        mounted: function () {
            let old_index = ''
            let new_index = ''
            var that = this
            $('table tbody').sortable({
                update: function (event, ui) {
                    new_index = ui.item.index()
                    if (!that.drag) {
                        let data_cut = that.items.splice(old_index, 1)[0]
                        let style_data_cut = that.style_data_list.splice(old_index, 1)[0]
                        that.items.splice(new_index, 0, data_cut)
                        that.style_data_list.splice(new_index, 0, style_data_cut)
                    } else {
                        that.$emit('drag', false)
                        let field_name = ui.item[0].textContent
                        console.log(field_name)
                        if (field_name == 'Spacer Field') {
                            let spacer_data = {
                                field_name: field_name,
                                order: ui.item.index()
                            }
                            that.items.splice(ui.item.index(), 0, spacer_data)
                            that.items_list.splice(ui.item.index(), 0, spacer_data)

                            let data = {
                                borderRadius: '5px',
                                width: this.canvas_width + 'px',
                                field_type: 'Input Box',
                                input_text_type: 'As Placeholder',
                                dropdown_values: [''],
                                background: '#ffffff',
                                borderColor: '#ffffff',
                                fontFamily: 'Arial',
                                fontSize: '12px',
                                color: '#000000',
                                field_opacity: '100',
                                outline_opacity: '100',
                                label_style: {
                                    fontFamily: 'Arial',
                                    fontSize: '12px',
                                    color: '#000000'
                                },
                                list_style: {
                                    fontFamily: 'Arial',
                                    fontSize: '12px',
                                    color: '#000000',
                                    width: (this.canvas_width - 30) + 'px',
                                }
                            }
                            that.style_data_list.splice(ui.item.index(), 0, data)
                            that.style_list.splice(ui.item.index(), 0, data)
                            $(ui.item).remove()

                        } else {
                            let index = 0
                            for (let i = 0; i < that.removed_items.length; i++) {
                                if (that.removed_items[i].field_name.trim() == field_name.trim()) {
                                    index = i
                                }
                            }
                            let data_removed = that.removed_items.splice(index, 1)[0]
                            that.items.splice(ui.item.index(), 0, data_removed)
                            that.items_list.splice(ui.item.index(), 0, data_removed)

                            let data = {
                                borderRadius: '5px',
                                width: this.canvas_width + 'px',
                                field_type: 'Input Box',
                                input_text_type: 'As Placeholder',
                                dropdown_values: [''],
                                background: '#ffffff',
                                borderColor: '#ffffff',
                                fontFamily: 'Arial',
                                fontSize: '12px',
                                color: '#000000',
                                field_opacity: '100',
                                outline_opacity: '100',
                                label_style: {
                                    fontFamily: 'Arial',
                                    fontSize: '12px',
                                    color: '#000000'
                                },
                                list_style: {
                                    fontFamily: 'Arial',
                                    fontSize: '12px',
                                    color: '#000000',
                                    width: (this.canvas_width - 30) + 'px',
                                }
                            }
                            that.style_data_list.splice(ui.item.index(), 0, data)
                            that.style_list.splice(ui.item.index(), 0, data)
                            $(ui.item).remove()
                        }
                    }
                },
                start: function (event, ui) {
                    old_index = ui.item.index()
                },
            });
        },
        watch: {
            style_data_list: {
                handler: function (val) {
                    this.layout_fields = []
                    for (let i = 0; i < this.items.length; i++) {
                        let with_placeholder = false
                        if (this.style_data_list[i].input_text_type == 'As Placeholder') {
                            with_placeholder = true
                        }
                        let data = {
                            guest_info_field_id: this.items[i].id,
                            type: this.style_data_list[i].field_type,
                            height: '',
                            width: this.style_data_list[i].width.replace("px", ""),
                            page_num: '1',
                            field_name: this.items[i].field_name,
                            order: i.toString(),
                            with_placeholder: with_placeholder,
                            font_family: this.style_data_list[i].fontFamily,
                            font_color: this.style_data_list[i].color,
                            font_size: this.style_data_list[i].fontSize.replace("px", ""),
                            background_color: this.style_data_list[i].background,
                            opacity: this.style_data_list[i].field_opacity,
                            border_color: this.style_data_list[i].borderColor,
                            label_color: this.style_data_list[i].label_style.color,
                            label_size: this.style_data_list[i].label_style.fontSize.replace("px", ""),
                            label_font_family: this.style_data_list[i].label_style.fontFamily,
                            list_font_color: this.style_data_list[i].list_style.color,
                            list_font_family: this.style_data_list[i].list_style.fontFamily,
                            list_font_size: this.style_data_list[i].list_style.fontSize.replace("px", ""),
                            field_values: this.style_data_list[i].dropdown_values,
                        }
                        this.layout_fields.push(data)
                    }
                    this.$emit('layout_fields', this.layout_fields)
                }, deep: true
            },
            items: function (val) {
                this.layout_fields = []
                for (let i = 0; i < val.length; i++) {
                    let with_placeholder = false
                    if (this.style_data_list[i].input_text_type == 'As Placeholder') {
                        with_placeholder = true
                    }
                    let data = {
                        guest_info_field_id: val[i].id,
                        type: this.style_data_list[i].field_type,
                        height: '',
                        width: this.style_data_list[i].width.replace("px", ""),
                        page_num: '1',
                        field_name: val[i].field_name,
                        order: i.toString(),
                        with_placeholder: with_placeholder,
                        font_family: this.style_data_list[i].fontFamily,
                        font_color: this.style_data_list[i].color,
                        font_size: this.style_data_list[i].fontSize.replace("px", ""),
                        background_color: this.style_data_list[i].background,
                        opacity: this.style_data_list[i].field_opacity,
                        border_color: this.style_data_list[i].borderColor,
                        label_color: this.style_data_list[i].label_style.color,
                        label_size: this.style_data_list[i].label_style.fontSize.replace("px", ""),
                        label_font_family: this.style_data_list[i].label_style.fontFamily,
                        list_font_color: this.style_data_list[i].list_style.color,
                        list_font_family: this.style_data_list[i].list_style.fontFamily,
                        list_font_size: this.style_data_list[i].list_style.fontSize.replace("px", ""),
                        field_values: this.style_data_list[i].dropdown_values,
                    }
                    this.layout_fields.push(data)
                }
                this.$emit('layout_fields', this.layout_fields)
                var that = this
//                this.$nextTick(function () {
//                    let old_index = ''
//                    let new_index = ''
//                    $('table tbody').sortable({
//                        receive: function (event, ui) {
//                            that.$emit('drag', false)
//                            let field_name = ui.item[0].textContent
//                            if (field_name == 'Spacer Field') {
//                                let spacer_data = {
//                                    field_name: field_name,
//                                    order: ui.item.index()
//                                }
//                                that.items.splice(ui.item.index(), 0, spacer_data)
//                                that.items_list.splice(ui.item.index(), 0, spacer_data)
//                            }
//                        }
//                    })
//                })
            }
        },
        props: {
            drag: {
                type: Boolean
            },
            removed_items: {
                type: Array
            },
            items: {
                type: Array,
                required: true
            },
            type: {
                type: String,
                required: true
            },
            input_text_type: {
                type: String,
            },
            style_data_list: {
                type: Array,
                required: true
            },
            canvas_width: {
                type: String
            }
        },
        data() {
            return {
                drag_val: false,
                items_list: [],
                layout_fields: [],
                style_list: [],
                ipadForm: {
                    marginTop: '15px',
                    marginLeft: '15px',
                    marginRight: '15px',
                    marginBottom: '10px',
                },
                show_input_display: {
                    position: 'absolute',
                    right: '10px',
                    display: 'block'
                }
            }
        },
        methods: {
            remove(index, data) {
                console.log(data)
                this.items.splice(index, 1)
                this.items_list.splice(index, 1)
                if (data.field_name != 'Spacer Field') {
                    this.$emit('remove', index, data)
                }
            },
            show_input(type) {
                if (type == 'show') {
                    this.show_input_display.display = 'block'
                } else {
                    this.show_input_display.display = 'none'
                }
            },
            set_selected(field_name, index) {
                this.$emit('set_selected', field_name, index)
            }
        }
    }
</script>