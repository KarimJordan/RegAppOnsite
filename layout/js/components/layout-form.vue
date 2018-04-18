<template>
    <div>
        <header class="header" role="banner">
            <nav class="navbar navbar-default nav-new">
                <div class="container">
                    <a class="logo pull-left" href="/events/"><img :src="require('../../../main/img/logo.png')"></a>
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

        <div class="container layout-editor">
            <h2>Layout Editor</h2>
            <a href="'/events/' + event_id + '/'" class="pull-right">
                <button class="btn btn-undo"><span class="fa fa-undo"></span>UNDO</button>
            </a>
            <ul class="nav nav-tabs">
                <li class="active"><a data-toggle="tab" :href="'/events/' + event_id + '/'">Registration Screen</a></li>
            </ul>

            <div class="tab-content">
                <br>

                <div id="registration" class="tab-pane fade in active">
                    <div class="col-md-3 editor-sidebar">
                        <!-- Sidebar Dropdown Tab Starts -->
                        <div class="button dropdown tab-dropdown settings-select">
                            <select class="tab_select" v-model="active_tab_name">
                                <option v-for="tab in tabs" :value="tab.value">{{tab.display}}</option>
                            </select>
                        </div>

                        <div class="tab-content clearfix">
                            <div v-if="isEqual('1generalsettings')">
                                <layout-general-settings
                                        :background_color="background_color"
                                        :canvas_color="canvas_color"
                                        :canvas_height="canvas_height.toString()"
                                        :canvas_width="canvas_width"
                                        :canvas_opacity="canvas_opacity"
                                        :layout_name="layout_name"
                                        @canvas_height="canvasHeight"
                                        @canvas_width="canvasWidth"
                                        @canvas_opacity="canvasOpacity"
                                        @background_color="backgroundColor"
                                        @canvas_color="canvasColor"
                                        @add_page="addPage"
                                        @layout_name="layoutName"
                                        @logo="logoImage"
                                        @background="backgroundImage"
                                        @hide_logo="hideLogo"
                                        @hide_background="hideBackground"
                                ></layout-general-settings>
                            </div>

                            <div v-if="isEqual('2buttons')">
                                <layout-button-settings
                                        :button_opacity="button_opacity"
                                        :button_color="button_color"
                                        :button_text_color="button_text_color"
                                        :button_font_size="button_font_size"
                                        :button_font_family="button_font_family"
                                        :submit_button_text="submit_button_text"
                                        :next_button_text="next_button_text"
                                        :back_button_text="back_button_text"
                                        :has_second_page="has_second_page"
                                        @button_opacity="buttonOpacity"
                                        @button_color="buttonColor"
                                        @button_text_color="buttonTextColor"
                                        @button_font_size="buttonFontSize"
                                        @button_font_family="buttonFontFamily"
                                        @submit_button_text="submitButtonText"
                                        @next_button_text="nextButtonText"
                                        @back_button_text="backButtonText"
                                        @button="buttonImageUpload"
                                        @hide_button="hideButton"
                                ></layout-button-settings>
                            </div>

                            <div v-if="isEqual('2fieldsettings')">
                                <layouut-field-settings
                                        :label_font_family="label_font_family"
                                        :label_font_size="label_font_size"
                                        :label_font_color="label_font_color"
                                        :input_font_family="input_font_family"
                                        :input_font_size="input_font_size"
                                        :input_font_color="input_font_color"
                                        :list_text_family="list_text_family"
                                        :list_text_font_size="list_text_font_size"
                                        :list_text_font_color="list_text_font_color"
                                        :apply_to_all="apply_to_all"
                                        :field_type="field_type"
                                        :field_width="field_width"
                                        :field_width_list="field_width_list"
                                        :field_color="field_color"
                                        :field_outline_color="field_outline_color"
                                        :input_text_type="input_text_type"
                                        :selected_field_value="selected_field_value"
                                        @label_font_family="labelFontFamily"
                                        @label_font_size="labelFontSize"
                                        @label_text_color="labelFontColor"
                                        @input_font_family="inputFontFamily"
                                        @input_font_size="inputFontSize"
                                        @input_font_color="inputFontColor"
                                        @list_text_family="listTextFamily"
                                        @list_text_font_size="listTextFontSize"
                                        @list_text_font_color="listTextFontColor"
                                        @apply_to_all="applyToAll"
                                        @field_type="fieldType"
                                        @list_values="listValues"
                                        @field_width="fieldWidth"
                                        @field_color="fieldColor"
                                        @field_outline_color="fieldOutlineColor"
                                        @input_text_type="inputTextType"
                                ></layouut-field-settings>
                            </div>

                            <div v-if="isEqual('3selection')">
                                <layout-remove-field-settings
                                        :removed_items="removed_items_list"
                                        @drag="drag"
                                ></layout-remove-field-settings>
                            </div>

                        </div>
                    </div>
                </div>

            </div>

            <div class="col-md-9 no-padding">

                <div class="ipad-header">
                    <h5>iPad Screen Views</h5>
                </div>
                <div class="ipad-screen" :style="ipad_screen">
                    <img v-show="!hide_background" :src="background_image" :style="background_style">
                    <div id="logo_placeholder" :style="logo_style">
                        <center><img id="logo-img" v-show="!hide_logo" :src="logo"></center>
                    </div>
                    <div :style="form_dragger" id="canvas_form">
                        <layout-field-cell
                                :style_data_list="style_data_list"
                                :type="field_type"
                                :input_text_type="input_text_type"
                                :items="guest_info_fields"
                                :removed_items="removed_items_list"
                                :drag="dragging"
                                :canvas_width="canvas_width"
                                @set_selected="set_selected"
                                @remove="remove"
                                @drag="drag"
                                @layout_fields="layout_fields"
                        ></layout-field-cell>

                        <div :style="submit_div_style">
                            <button v-if="button_hide" :style="submit_button_style">{{submit_button_text}}</button>
                            <img v-if="!button_hide" :style="button_image_style" :src="button_image"/>
                        </div>

                        <div v-if="has_second_page" :style="back_div_style">
                            <button :style="submit_button_style">{{back_button_text}}</button>
                            <button :style="submit_button_style">{{back_button_text}}</button>
                        </div>


                    </div>
                </div>
            </div>
        </div>

        <center>
            <ul class="list-inline save-layout">
                <li>
                    <button @click="save_layout" class="btn btn-block btn-create-event btn-ignore" type="button">
                        SAVE
                    </button>
                </li>
            </ul>
        </center>

    </div>

</template>
<style>
    @import "../../../node_modules/gridstack/dist/gridstack-extra.css";
    @import '../../../node_modules/jquery-ui/themes/base/core.css';
    @import '../../../node_modules/jquery-ui/themes/base/theme.css';
    @import '../../../node_modules/jquery-ui/themes/base/menu.css';
    @import '../../../node_modules/jquery-ui/themes/base/resizable.css';

    .tab_select {
        margin-bottom: 0 !important;
    }
</style>
<script type="text/babel">

    import axios from 'axios'

    import LayoutGeneralSettings from './layout-general-settings.vue'
    import LayoutButtonSettings from "./layout-button-settings.vue"
    import LayouutFieldSettings from './layout-field-settings.vue'
    import LayoutRemoveFieldSettings from './layout-remove-field-settings.vue'

    import gridstack from 'gridstack'

    //    import sample from '../../../node_modules/webpack-jquery-ui/draggable'

    import draggrable from '../../../node_modules/jquery-ui/ui/widgets/draggable'
    import resizable from '../../../node_modules/jquery-ui/ui/widgets/resizable'

    import LayoutFieldCell from './layout-field-cell.vue'

    export default {
        name: 'LayoutForm',
        components: {
            LayoutButtonSettings,
            LayoutGeneralSettings,
            LayouutFieldSettings,
            LayoutRemoveFieldSettings,
            LayoutFieldCell
        },
        data() {
            return {
                layout,
                csrf,
                event_id,
                removed_fields,
                is_update: false,
                output_data: {},
                guest_info_fields,
                active_tab_name: '1generalsettings',
                tabs: [
                    {value: '1generalsettings', display: 'General Settings'},
                    {value: '2buttons', display: 'Buttons'},
                    {value: '2fieldsettings', display: 'Field Settings'},
                    {value: '3selection', display: 'Field Selection'}
                ],

                // form styles
                form_dragger: {
                    borderRadius: '5px',
                    position: 'absolute',
                    background: '#c76868',
                },

                logo_style: {
                    position: 'absolute'
                },
                background_style: {
                    position: 'absolute',
                    width: '100%',
                    height: '576px'
                },

                ipad_screen: {
                    width: '100%',
                    height: '576px'
                },

                // field style
                style_data: {
                    borderRadius: '5px'
                },
                style_data_list: [],

                // submit button style
                submit_div_style: {
                    margin: '13px',
                    position: 'absolute',
                    right: 0,
                    bottom: 0,
                    float: 'right',
                    paddingTop: '10px',
                    padding: 0
                },

                back_div_style: {
                    margin: '13px',
                    position: 'absolute',
                    left: 0,
                    bottom: 0,
                    float: 'left',
                    paddingTop: '10px',
                    padding: 0
                },
                button_image_style: {
                    width: '100px',
                    borderRadius: '5px',
                    border: 'none',
                },
                submit_button_style: {
                    width: '100px',
                    borderRadius: '5px',
                    border: 'none',
                    padding: '10px 20px',
                    background: '#000000',
                    color: '#ffffff'
                },

                dragging: false,
                layout_fields_list: [],

                // removed items
                removed_items_list: [],

                // general settings data
                background_color: '#ffffff',
                canvas_color: '#c76868',
                canvas_height: '100',
                canvas_width: '500',
                canvas_opacity: '50',
                canvas_pos_x: '100',
                canvas_pos_y: '100',
                layout_name: '',
                logo: '',
                background_image: '',
                hide_logo: true,
                hide_background: true,

                //button settings data
                button_opacity: '100',
                button_color: '#000000',
                button_text_color: '#ffffff',
                button_font_size: '12',
                button_font_family: 'Arial',
                button_image: '',
                button_hide: true,
                submit_button_text: 'SUBMIT',
                next_button_text: 'NEXT',
                back_button_text: 'BACK',
                has_second_page: false,

                //field settings data
                label_font_family: 'Arial',
                label_font_size: '12',
                label_font_color: '#000000',
                input_font_family: 'Arial',
                input_font_size: '12',
                input_font_color: '#000000',
                list_text_family: 'Arial',
                list_text_font_size: '12',
                list_text_font_color: '#000000',
                apply_to_all: false,
                field_type: 'Input Box',
                field_width: '400',
                field_width_list: [],
                field_color: '#ffffff',
                field_outline_color: '#ffffff',
                input_text_type: 'As Placeholder',
                selected_field_value: 'NOTHING',
                selected_index: null
            }
        },
        mounted: function () {
            var that = this

            $('#logo_placeholder').draggable({
                containment: "parent",
                refreshPositions: true,
                stop: function (event, ui) {
//                    that.logo_pos_x = parseFloat(ui.position.left) / 0.33
                    that.logo_pos_x = ui.position.left
                    that.logo_pos_y = ui.position.top
                }
            })

//            $('#logo-img').resizable({
//                handles: "n, e, s, w, se",
//                resize: function (event, ui) {
//                    that.logo_width = ui.size.width.toString()
//                    that.logo_height = ui.size.height.toString()
//                }
//            })


            $('#canvas_form').draggable({
                containment: "parent",
                refreshPositions: true,
                stop: function (event, ui) {
//                    that.canvas_pos_x = parseFloat(ui.position.left) / 0.33
                    that.canvas_pos_x = ui.position.left
                    that.canvas_pos_y = ui.position.top
//                    that.form_dragger.top = that.canvas_pos_y
                }
            })

            $('#canvas_form').resizable({
                containment: "parent",
                handles: "n, e, s, w, se",
                resize: function (event, ui) {
                    that.canvas_width = ui.size.width.toString()
//                    that.canvas_width = ((ui.size.width * 0.19) + ui.size.width).toString()
                    that.canvas_height = ui.size.height.toString()
                    for (let i = 0; i < that.guest_info_fields.length; i++) {
                        that.style_data_list[i].width = (ui.size.width - 30) + 'px'
                    }

                    //field_width_list
                    let display = 1
                    that.field_width_list = []
                    let dividedWidth = Math.round((ui.size.width - 30) / 4)
                    for (var i = 1; i <= 4; i++) {
                        that.field_width_list.push(
                            {
                                'display': display,
                                'value': Math.round(dividedWidth * i)
                            }
                        )
                        display++
                    }

                }
            })
        },
        created() {

            // upon update values
            if (this.layout.layout_name != undefined) {
                this.is_update = true
            }

            // initial values
            if (this.is_update) {
                //removed fields

                if (this.removed_fields.length > 0) {
                    this.removed_items_list = this.removed_fields
                }

                // layout name
                this.layout_name = this.layout.layout_name

                // layout logo
                if (this.layout.logo != '') {
                    this.logo = this.layout.logo
                    this.hide_logo = false
                }
                // layout background image
                if (this.layout.background_image != '') {
                    this.background_image = this.layout.background_image
                    this.hide_background = false
                }

                // logo pos
                this.logo_pos_x = this.layout.logo_pos_x
                this.logo_pos_y = this.layout.logo_pos_y
                this.logo_style.top = this.logo_pos_y + 'px'
                this.logo_style.left = this.logo_pos_x + 'px'

                // layout background color
                this.background_color = this.layout.background_color

                // form height
                this.canvas_height = this.layout.canvas_height

                // form width
                this.canvas_width = this.layout.canvas_width
                this.field_width = (this.canvas_width - 30) + 'px'

                // canvas color
                this.canvas_color = this.hexToRgbA(this.layout.canvas_background_color, this.canvas_opacity / 100)

                // canvas posx
                this.canvas_pos_x = this.layout.canvas_pos_x
                this.form_dragger.left = this.canvas_pos_x + 'px'

                // canvas posy
                this.canvas_pos_y = this.layout.canvas_pos_y
                this.form_dragger.top = this.canvas_pos_y + 'px'

                // form opacity
                this.canvas_opacity = this.layout.canvas_opacity
                this.form_dragger.background = this.hexToRgbA(this.canvas_color, this.canvas_opacity / 100)

                if (this.layout.button_image != ''){
                    this.button_image = this.layout.button_image
                }

//                let heightConst = 50
//                this.canvas_height = 0
//                for (const i in this.guest_info_fields) {
//                    this.canvas_height += heightConst
//                }

                //create style data for fields

                for (let field of this.guest_info_fields) {
                    let text_type = 'As Placeholder'
                    console.log(field.with_placeholder)
                    if (!field.with_placeholder) {
                        text_type = 'As Label'
                    }

                    let data = {
                        borderRadius: '5px',
                        width: (this.canvas_width - 30) + 'px',
                        field_type: field.type,
                        input_text_type: text_type,
                        background: field.background_color,
                        borderColor: field.border_color,
                        fontFamily: field.font_family,
                        fontSize: field.font_size,
                        color: field.font_color,
                        field_opacity: '100',
                        outline_opacity: '100',
                        label_style: {
                            fontFamily: field.label_font_family,
                            fontSize: field.label_size,
                            color: field.label_color
                        },
                        list_style: {
                            fontFamily: field.list_font_family,
                            fontSize: field.list_font_size,
                            color: field.list_font_color,
                            width: (this.canvas_width - 30) + 'px',
                        },
                        dropdown_values: ['']
                    }
                    this.style_data_list.push(data)
                }

            } else {
                // initial canvas height
                let heightConst = 50
                this.canvas_height = 0
                for (const i in this.guest_info_fields) {
                    this.canvas_height += heightConst
                }

                //create style data for fields
                for (let field in this.guest_info_fields) {
                    let data = {
                        borderRadius: '5px',
                        width: (this.canvas_width - 30) + 'px',
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
                    this.style_data_list.push(data)
                }
            }
            // upon update end


            //field_width_list
            let display = 1
            this.field_width_list = []
            let dividedWidth = Math.round((this.canvas_width - 30) / 4)
            for (var i = 1; i <= 4; i++) {
                this.field_width_list.push(
                    {
                        'display': display,
                        'value': Math.round(dividedWidth * i)
                    }
                )
                display++
            }
        },
        watch: {
            canvas_height: function (val) {
                this.canvas_height = val
            },
            field_width_list: function (val) {
                this.field_width_list = val
            }
        },
        methods: {
            dataRemoved(data_removed, index) {
                this.guest_info_fields.push(data_removed)

                this.style_data_list.push(data)
            },
            hideBackground() {
                this.hide_background = true
                this.background_image = ''
            },
            hideLogo() {
                this.hide_logo = true
                this.logo = ''

            },
            hideButton() {
                this.button_hide = true
                this.button_image = ''
            },
            buttonImageUpload(val) {
                this.button_hide = false
                this.button_image = val
            },
            logoImage(val) {
                this.hide_logo = false
                this.logo = val
            },
            backgroundImage(val) {
                this.hide_background = false
                this.background_image = val
            },
            layout_fields(val) {
                this.layout_fields_list = val
                console.log(this.layout_fields_list)
            },
            save_layout() {
                let url = '/layouts/'
                const method = 'POST'
                const redirect = '/events/' + this.event_id + '/'

                let layout_fields = []
                let layout_field_values = []

                const data = {
                    '_method': 'create',
                    'event_id': parseInt(this.event_id),
                    'background_image': this.background_image,
                    'background_color': this.background_color,
                    'logo': this.logo,
                    'logo_pos_x': this.logo_pos_x,
                    'logo_pos_y': this.logo_pos_y,
                    'logo_width': '100',
                    'logo_height': '100',
                    'layout_type': '0',
                    'canvas_height': this.canvas_height.toString(),
                    'canvas_width': this.canvas_width.toString(),
                    'canvas_padding': '0',
                    'canvas_background_color': this.canvas_color,
                    'canvas_opacity': this.canvas_opacity,
                    'canvas_pos_x': this.canvas_pos_x,
                    'canvas_pos_y': this.canvas_pos_y,
                    'button_image': this.button_image,
                    'button_color': this.button_color,
                    'button_opacity': this.button_opacity,
                    'button_text_color': this.button_text_color,
                    'submit_button_text': this.submit_button_text,
                    'next_button_text': this.next_button_text,
                    'back_button_text': this.back_button_text,
                    'button_font_family': this.button_font_family,
                    'button_font_size': this.button_font_size,
                    'layout_name': this.layout_name,
                    'layout_fields': this.layout_fields_list
                }

                if (this.is_update) {
                    data._method = 'update'
                    url = '/layouts/' + this.layout.id + '/'
                }
                console.log('kljhgv')
                console.log(data.layout_fields)

                this.output_data = data

                const request = {
                    method: method,
                    url: url,
                    data: data,
                    headers: {'X-CSRFToken': this.csrf}
                }

                axios(request)
                    .then((response) => {
//                        console.log(response)
                        window.location.replace(redirect);
                    })
                    .catch((error) => {
                        console.log(error)
                    })
            },
            drag(val) {
                this.dragging = val
            },
            update_items(items) {

                this.guest_info_fields = items

                const url = ''
                const method = 'post'
                const data = items
                const redirect = '/guests/fields/' + this.event_id + '/'
                const request = {
                    method: 'post',
                    url: redirect,
                    data: items,
                    headers: {'X-CSRFToken': this.csrf}
                }

//                axios(request)
//                    .then((response) => {
//                        console.log(response)
////                        window.location.replace(redirect);
//                    })
//                    .catch((error) => {
//                        console.log(error)
//                    })
            },
            remove(index, item) {
                this.removed_items_list.push(item)
            },
            set_selected(field_name, index) {
                this.selected_field_value = field_name
                this.selected_index = index
            },

            // field settings
            labelFontFamily(val) {
                this.label_font_family = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].label_style.fontFamily = val
                }
            },
            labelFontSize(val) {
                this.label_font_size = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].label_style.fontSize = val + 'px'
                }
            },
            labelFontColor(val) {
                this.label_font_color = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].label_style.color = val
                }
            },
            inputFontFamily(val) {
                this.input_font_family = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].fontFamily = val
                }
            },
            inputFontSize(val) {
                this.input_font_size = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].fontSize = val + 'px'
                }
            },
            inputFontColor(val) {
                this.input_font_color = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].color = val
                }
            },
            listTextFamily(val) {
                this.list_text_family = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].list_style.fontFamily = val
                }
            },
            listTextFontSize(val) {
                this.list_text_font_size = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].list_style.fontSize = val + 'px'
                }
            },
            listTextFontColor(val) {
                this.list_text_font_color = val
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].list_style.color = val
                }
            },
            applyToAll(val) {
                this.apply_to_all = val
            },
            fieldType(val) {
                this.field_type = val
                if (this.selected_index != null && !this.apply_to_all) {
                    this.style_data_list[this.selected_index].field_type = val
                } else if (this.apply_to_all) {
                    for (let i = 0; i < this.guest_info_fields.length; i++) {
                        this.style_data_list[i].field_type = val
                    }
                }
            },
            listValues(val) {
                if (this.selected_index != null && !this.apply_to_all) {
                    this.style_data_list[this.selected_index].dropdown_values = val
                }
            },
            inputTextType(val) {
                this.input_text_type = val
                if (this.selected_index != null && !this.apply_to_all) {
                    this.style_data_list[this.selected_index].input_text_type = val
                } else if (this.apply_to_all) {
                    for (let i = 0; i < this.guest_info_fields.length; i++) {
                        this.style_data_list[i].input_text_type = val
                    }
                }
            },
            fieldWidth(val) {
                this.field_width = val.toString()
                if (this.selected_index != null && !this.apply_to_all) {
                    this.style_data_list[this.selected_index].width = val + 'px'
                } else if (this.apply_to_all) {
                    for (let i = 0; i < this.guest_info_fields.length; i++) {
                        this.style_data_list[i].width = val + 'px'
                    }
                }
            },
            fieldColor(val, opacity) {
                this.field_color = val
                if (this.selected_index != null) {
                    this.style_data_list[this.selected_index].background = val
                    this.style_data_list[this.selected_index].field_opacity = opacity
                } else if (this.apply_to_all) {
                    for (let i = 0; i < this.guest_info_fields.length; i++) {
                        this.style_data_list[i].background = val
                        this.style_data_list[i].field_opacity = opacity
                    }
                }
            },
            fieldOutlineColor(val, opacity) {
                this.field_outline_color = val
                if (this.selected_index != null && !this.apply_to_all) {
                    this.style_data_list[this.selected_index].borderColor = val
                    this.style_data_list[this.selected_index].outline_opacity = opacity
                } else if (this.apply_to_all) {
                    for (let i = 0; i < this.guest_info_fields.length; i++) {
                        this.style_data_list[i].borderColor = val
                        this.style_data_list[i].outline_opacity = opacity
                    }
                }
            },

            //button settings
            addPage() {
                this.has_second_page = true
            },
            buttonOpacity(val) {
                this.button_opacity = val
                this.submit_button_style.background = this.hexToRgbA(this.button_color, val / 100)
            },
            buttonColor(val) {
                this.button_color = val
                this.submit_button_style.background = val
            },
            buttonTextColor(val) {
                this.button_text_color = val
                this.submit_button_style.color = val
            },
            buttonFontSize(val) {
                this.button_font_size = val
                this.submit_button_style.fontSize = val + 'px'
                this.submit_button_style.width = (100 + parseInt(val)) + 'px'
            },
            buttonFontFamily(val) {
                this.button_font_family = val
                this.submit_button_style.fontFamily = val
            },
            submitButtonText(val) {
                this.submit_button_text = val
                this.submit_button_style.width = (100 + this.submit_button_text.length) + 'px'
            },
            nextButtonText(val) {
                this.next_button_text = val
            },
            backButtonText(val) {
                this.back_button_text = val
            },


            // general settings
            layoutName(val) {
                this.layout_name = val
//                if (this.layout.layout_name != ''){
//                    this.layout_name = this.layout.layout_name
//                }
            },
            canvasHeight(val) {
                this.canvas_height = val
                this.form_dragger.height = val + 'px'
            },
            canvasWidth(val) {
                this.canvas_width = val
                this.form_dragger.width = val + 'px'

//                console.log(this.style_data_list)
                for (let i = 0; i < this.guest_info_fields.length; i++) {
                    this.style_data_list[i].width = (val - 30) + 'px'
                }

                //field_width_list
                let display = 1
                this.field_width_list = []
                let dividedWidth = Math.round((val - 30) / 4)
                for (var i = 1; i <= 4; i++) {
                    this.field_width_list.push(
                        {
                            'display': display,
                            'value': Math.round(dividedWidth * i)
                        }
                    )
                    display++
                }

            },
            canvasOpacity(val) {
                this.canvas_opacity = val
                this.form_dragger.background = this.hexToRgbA(this.canvas_color, val / 100)
            },
            backgroundColor(val) {
                this.background_color = val
                this.ipad_screen.background = val
            },
            canvasColor(val) {
                this.canvas_color = val
                this.form_dragger.background = val
            },

            // utilities
            isEqual(name) {
                return this.active_tab_name === name
            },
            hexToRgbA(hex, alpha) {
                if (hex != undefined) {
                    var c = hex.substring(1).split('');
                    if (c.length == 3) {
                        c = [c[0], c[0], c[1], c[1], c[2], c[2]];
                    }
                    c = '0x' + c.join('');
                    return 'rgba(' + [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',') + ',' + alpha + ')';
                }
            },
        }
    }
</script>