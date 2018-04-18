<template>
    <div class="wrapper-sidebar">
        <h5>General Field Settings</h5>
        <h5 class="subheader-menu">Label Text</h5>
        <div class="row">
            <div class=" col-md-6 no-padding">
                <label>Font & Size</label>
            </div>
            <div class="col-md-3 no-padding ">
                <select v-model="label_font_family_value" class="dropdown-toggle">
                    <option v-for="ffamily in fontFamilyList" :value="ffamily">
                        {{ffamily}}
                    </option>
                </select>
            </div>
            <div class="col-md-3 no-padding">
                <select v-model="label_font_size_value" class="dropdown-toggle">
                    <option v-for="size in fontSizeList" :value="size">{{size}}</option>
                </select>
            </div>
        </div>

        <div class="row">
            <div class="thead col-md-6 no-padding">
                <label>Color & Opacity</label>
            </div>
            <div class="example col-md-3 form-h opacity-range">
                <input type="text" id="label_text_color">
                <input type="hidden" v-model="label_text_color_value"/>
            </div>
            <div class="col-md-3 form-h opacity-range">
                <input class="form-control form-opacity" v-model="label_text_color_display_value">
            </div>
        </div>

        <h5 class="subheader-menu">Input Text</h5>

        <div class="row">
            <div class="thead col-md-6 no-padding">
                <label>Font & Size</label>
            </div>
            <div class="col-md-3 no-padding ">
                <select v-model="input_font_family_value" class="dropdown-toggle">
                    <option v-for="ffamily in fontFamilyList" :value="ffamily">
                        {{ffamily}}
                    </option>
                </select>
            </div>
            <div class="col-md-3 no-padding">
                <select v-model="input_font_size_value" class="dropdown-toggle">
                    <option v-for="size in fontSizeList" :value="size">{{size}}</option>
                </select>
            </div>
        </div>

        <div class="row">
            <div class="thead col-md-6 no-padding">
                <label>Color & Opacity</label>
            </div>
            <div class="example col-md-3 form-h opacity-range">
                <input type="text" id="input_text_color">
                <input type="hidden" v-model="input_font_color_value"/>
            </div>
            <div class="col-md-3 form-h opacity-range">
                <input class="form-control form-opacity" v-model="input_text_color_display_value">
            </div>
        </div>

        <h5 class="subheader-menu">List Text</h5>
        <div class="row">
            <div class="thead col-md-6 no-padding">
                <label>Font & Size</label>
            </div>
            <div class="col-md-3 no-padding ">
                <select v-model="list_text_family_value" class="dropdown-toggle">
                    <option v-for="ffamily in fontFamilyList" :value="ffamily">
                        {{ffamily}}
                    </option>
                </select>
            </div>
            <div class="col-md-3 no-padding">
                <select v-model="list_text_font_size_value" class="dropdown-toggle">
                    <option v-for="size in fontSizeList" :value="size">{{size}}</option>
                </select>
            </div>
        </div>

        <div class="row">
            <div class="thead col-md-6 no-padding">
                <label>Color & Opacity</label>
            </div>
            <div class="example col-md-3 form-h opacity-range">
                <input type="text" id="list_text_color">
                <input type="hidden" v-model="list_text_font_color_value"/>
            </div>
            <div class="col-md-3 form-h opacity-range">
                <input class="form-control form-opacity" v-model="list_text_font_color_display_value">
            </div>
        </div>

        <hr style="margin: 0;">
        <h5>Individual Field Setting</h5>

        <h5 class="field-selected">{{selected_field_value}} - SELECTED</h5>
        <div class="row">
            <label class="checkbox-inline">
                <input type="checkbox" v-model="apply_to_all_value">APPLY TO ALL
            </label>
        </div>
        <br>
        <div class="row">
            <div class=" col-md-6 no-padding">
                <label>Input Label</label>
            </div>
            <div class="col-md-6 no-padding form-h">
                <select class="dropdown-toggle" v-model="input_text_type_value">
                    <option v-for="type in input_text_type_list" :value="type">{{type}}</option>
                </select>
            </div>
        </div>
        <div class="row">
            <div class=" col-md-6 no-padding">
                <label>Field Type</label>
            </div>
            <div class="col-md-6 no-padding form-h">
                <select class="dropdown-toggle" v-model="field_type_value">
                    <option v-for="type in field_type_list" :value="type">{{type}}</option>
                </select>
            </div>
        </div>


        <div class="row">
            <div class=" col-md-6 no-padding">
                <label>Field Width</label>
            </div>
            <div class="col-md-6 no-padding ">
                <select class="dropdown-toggle" v-model="field_width_value">
                    <option v-for="width in field_width_list" :value="width.value">{{width.display}}</option>
                </select>
            </div>
        </div>

        <div v-if="field_type_value == 'Dropdown' || field_type_value == 'Checkbox' || field_type_value == 'Radio Button'"
             class="input-options">
            <span class="color-white">Field values "seperate with comma(,)"</span>
            <input v-model="list_values_text" type='text' size='20'
                   style="margin: 0px !important;"/>
            <span v-if="list_values.length > 3" id="error-msg"
                  style="color:red;">Maximum of 3 options.</span>
        </div>

        <h5 class="subheader-menu">Field Box</h5>
        <div class="row">
            <div class=" col-md-6 no-padding">
                <label>Color & Opacity</label>
            </div>
            <div class="example col-md-3 form-h opacity-range">
                <input type="text" id="field_color">
                <input type="hidden" v-model="field_color_value"/>
            </div>
            <div class="col-md-3 form-h opacity-range">
                <input class="form-control form-opacity" v-model="field_color_display_value">
            </div>
        </div>

        <h5 class="subheader-menu">Field Outline</h5>
        <div class="row">
            <div class=" col-md-6 no-padding">
                <label>Color & Opacity</label>
            </div>
            <div class="example col-md-3 form-h opacity-range">
                <input type="text" id="field_outline_color">
                <input type="hidden" v-model="field_outline_color_value"/>
            </div>
            <div class="col-md-3 form-h opacity-range">
                <input class="form-control form-opacity" v-model="field_outline_color_display_value">
            </div>
        </div>

    </div>
</template>
<style>
    @import "../../../node_modules/spectrum-colorpicker/spectrum.css";
</style>
<script type="text/babel">

    import spectrum from 'spectrum-colorpicker'

    import $ from 'jquery'

    export default {
        name: 'LayoutFieldSettings',
        props: {
            label_font_family: {
                type: String
            },
            label_font_size: {
                type: String
            },
            label_font_color: {
                type: String
            },
            input_font_family: {
                type: String
            },
            input_font_size: {
                type: String
            },
            input_font_color: {
                type: String
            },
            list_text_family: {
                type: String
            },
            list_text_font_size: {
                type: String
            },
            list_text_font_color: {
                type: String
            },
            apply_to_all: {
                type: Boolean
            },
            field_type: {
                type: String
            },
            field_width: {
                type: String
            },
            field_width_list: {
                type: Array
            },
            field_color: {
                type: String
            },
            field_outline_color: {
                type: String
            },
            input_text_type: {
                type: String
            },
            selected_field_value: {
                type: String
            }
        },
        created() {
            this.label_font_family_value = this.label_font_family
            this.label_font_size_value = this.label_font_size
            this.label_text_color_value = this.label_font_color
            this.input_font_family_value = this.input_font_family
            this.input_font_size_value = this.input_font_size
            this.input_font_color_value = this.input_font_color
            this.list_text_family_value = this.list_text_family
            this.list_text_font_size_value = this.list_text_font_size
            this.list_text_font_color_value = this.list_text_font_color
            this.apply_to_all_value = this.apply_to_all
            this.field_type_value = this.field_type
            this.field_width_value = this.field_width
            this.field_width_list_value = this.field_width_list_value
            this.field_color_value = this.field_color
            this.field_outline_color_value = this.field_outline_color
            this.input_text_type_value = this.input_text_type
        },
        watch: {
            selected_field_value: function (val) {
                this.selected_field_value = val
            },
            label_font_family_value: function (val) {
                this.$emit('label_font_family', val)
                this.label_font_family_value = val
            },
            label_font_size_value: function (val) {
                this.$emit('label_font_size', val)
                this.label_font_size_value = val
            },
            label_text_color_value: function (val) {
                this.$emit('label_text_color', val)
                this.label_text_color_value = val
            },
            input_font_family_value: function (val) {
                this.$emit('input_font_family', val)
                this.input_font_family_value = val
            },
            input_font_size_value: function(val){
                this.input_font_size_value = val
                this.$emit('input_font_size', val)
            },
            input_font_color_value: function (val) {
                this.$emit('input_font_color', val)
                this.input_font_color_value = val
            },
            list_text_family_value: function (val) {
                this.$emit('list_text_family', val)
                this.list_text_family_value = val
            },
            list_text_font_size_value: function (val) {
                this.$emit('list_text_font_size', val)
                this.list_text_font_size_value = val
            },
            list_text_font_color_value: function (val) {
                this.$emit('list_text_font_color', val)
                this.list_text_font_color_value = val
            },
            apply_to_all_value: function (val) {
                this.$emit('apply_to_all', val)
                this.apply_to_all_value = val
            },
            field_type_value: function (val) {
                this.$emit('field_type', val)
                this.field_type_value = val
            },
            list_values_text: function (val) {
                this.list_values_text = val
                this.list_values = this.list_values_text.split(',')
                this.$emit('list_values', this.list_values)
            },
            field_width_value: function (val) {
                this.$emit('field_width', val)
                this.field_width_value = val
            },
            field_color_value: function (val) {
                this.$emit('field_color', val, this.field_color_opacity)
                this.field_color_value = val
            },
            field_outline_color_value: function (val) {
                this.$emit('field_outline_color', val, this.field_outline_opacity)
                this.field_outline_color_value = val
            },
            input_text_type_value: function (val) {
                this.$emit('input_text_type', val)
                this.input_text_type_value = val
            }
        },
        data() {
            return {
                label_font_family_value: '',
                label_font_size_value: '',
                label_text_color_value: '',
                label_text_color_display_value: '',
                input_font_family_value: '',
                input_font_size_value: '',
                input_font_color_value: '',
                input_text_color_display_value: '',
                list_text_family_value: '',
                list_text_font_size_value: '',
                list_text_font_color_value: '',
                list_text_font_color_display_value: '',
//                selected_field_value: 'NOTHING - SELECTED',
                apply_to_all_value: false,
                field_type_value: '',
                field_type_list: [
                    'Input Box',
                    'Dropdown',
                    'Checkbox',
                    'Radio Button'
                ],
                list_values_text: '',
                list_values: [],
                field_width_value: '',
                field_width_list_value: [],
                field_color_value: '',
                field_color_display_value: '',
                field_color_opacity: '',
                field_outline_color_value: '',
                field_outline_color_display_value: '',
                field_outline_opacity: '',
                input_text_type_value: 'As Label',
                input_text_type_list: [
                    'As Label',
                    'As Placeholder'
                ],
                fontFamilyList: [
                    'Arial',
                    'Calibri',
                    'Calisto',
                    'Cambria',
                    'Comics Sans',
                    'Constantia',
                    'Copperplate Gothic'
                ],
                fontSizeList: [
                    '12', '13', '14', '15',
                    '16', '17', '18', '19',
                    '20', '21', '22', '23',
                    '24', '25', '26', '27',
                    '28'
                ]
            }
        },
        mounted: function () {
            //text color and opacity
            var that = this
            $('#label_text_color').spectrum({
                color: this.label_text_color_value,
                preferredFormat: "hex",
                showButtons: false,
                showAlpha: true,
                showInput: true,
                move: function (color) {
                    that.label_text_color_value = color.toRgbString()
                    that.label_text_color_display_value = color.toHexString()
                }
            })

            $('#input_text_color').spectrum({
                color: this.input_font_color_value,
                preferredFormat: "hex",
                showButtons: false,
                showAlpha: true,
                showInput: true,
                move: function (color) {
                    that.input_font_color_value = color.toRgbString()
                    that.input_text_color_display_value = color.toHexString()
                }
            })

            $('#list_text_color').spectrum({
                color: this.list_text_font_color_value,
                preferredFormat: "hex",
                showButtons: false,
                showAlpha: true,
                showInput: true,
                move: function (color) {
                    that.list_text_font_color_value = color.toRgbString()
                    that.list_text_font_color_display_value = color.toHexString()
                }
            })

            $('#field_color').spectrum({
                color: this.field_color_value,
                preferredFormat: "hex",
                showButtons: false,
                showAlpha: true,
                showInput: true,
                move: function (color) {
                    that.field_color_opacity = color.getAlpha() * 100
                    that.field_color_value = color.toRgbString()
                    that.field_color_display_value = color.toHexString()
                }
            })

            $('#field_outline_color').spectrum({
                color: this.field_outline_color_value,
                preferredFormat: "hex",
                showButtons: false,
                showAlpha: true,
                move: function (color) {
                    that.field_outline_opacity = color.getAlpha() * 100
                    that.field_outline_color_value = color.toRgbString()
                    that.field_outline_color_display_value = color.toHexString()
                }
            })
        }
    }
</script>