<template>
    <div>
        <!--Header-->
        <header class="header" role="banner">
            <nav class="navbar navbar-default nav-new">
                <div class="container">
                    <!--<div class="navbar-header">-->
                    <!--<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">-->
                    <!--<span class="icon-bar"></span>-->
                    <!--<span class="icon-bar"></span>-->
                    <!--<span class="icon-bar"></span>-->
                    <!--</button>-->
                    <!--<a class="logo" href=""><img src="content/img/logo.png"></a>-->
                    <!--</div>-->
                    <ul class="collapse nav nav-green list-inline">
                        <li>
                            <a href="/events/1">
                                <span class="icon icon-irs-icn"></span>
                                EVENTS DETAIL
                            </a>
                        </li>
                        <li>
                            <form>
                                <a href="#"><span class="icon icon-reffler-icn"></span>E-RAFFLER</a>
                            </form>
                        </li>
                        <li class="logout">
                            <form>
                                <a href="#"><span class="icon icon-power"></span>Logout</a>
                            </form>
                        </li>
                    </ul>
                </div>
            </nav>
        </header>

        <!--Body-->
        <div class="container layout-editor">
            <h2>Layout Editor</h2>
            <ul class="nav nav-tabs">
                <li class="active"><a data-toggle="tab" href="#registration">Registration Screen</a></li>
            </ul>

            <div class="tab-content">
                <br>

                <!-- First Tab - REGISTRATION STARTS HERE -->
                <div id="registration" class="tab-pane fade in active">
                    <!-- Sidebar Main Starts here -->
                    <div class="col-md-3 editor-sidebar">
                        <!-- Sidebar Dropdown Tab Starts -->
                        <div class="button dropdown tab-dropdown">
                            <select v-model="activeTabName" id="tabselector">
                                <option v-for="tab in tabs" :value="tab.value">{{ tab.displayName }}</option>
                            </select>

                        </div>
                        <!-- Sidebar Dropdown Tab Ends -->

                        <!---->
                        <div class="tab-content clearfix">
                            <!-- Sidebar Canvas Starts -->

                            <!--Canvas and Form Setings-->
                            <div v-show="isEqual('1generalsettings')">
                                <div class="wrapper-sidebar">
                                    <h5>Canvas</h5>
                                    <div class="row">

                                        <!--Logo Image-->
                                        <div class="col-md-6 no-padding">
                                            <label>Logo Image</label>
                                        </div>
                                        <div class="col-md-4 no-padding">
                                            <ul class="list-inline upload-list">
                                                <li class="fileUpload upload-btn">
                                                    <center><span class="icon icon-image-upload"></span></center>
                                                    <input type="file" class="upload"/>
                                                </li>
                                            </ul>
                                        </div>

                                        <!--Background Image-->
                                        <div class="col-md-6 no-padding ">
                                            <label>Background Image</label>
                                        </div>
                                        <div class="col-md-4 no-padding">
                                            <ul class="list-inline upload-list">
                                                <li class="fileUpload upload-btn">
                                                    <center><span class="icon icon-image-upload"></span></center>
                                                    <input type="file" class="upload"/>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-2 no-padding upload-list">
                                            <a href="#"><span class="pull-right icon-trash"></span> </a>
                                        </div>

                                        <!--Background Color-->
                                        <div class="thead col-md-6 no-padding">
                                            <label>Background Color</label>
                                        </div>
                                        <div class="thead col-md-6 no-padding">
                                            <input type="hidden" v-model="colors"/>
                                            <input type="text" id="background_color">
                                        </div>

                                    </div>
                                    <hr class="hr-breaker">
                                    <!--Form Information-->
                                    <h5>FORM</h5>

                                    <div class="row">
                                        <!-- Form Height -->
                                        <div class="col-md-6 no-padding">
                                            <label>Height</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="canvasHeight" class="form-control form-opacity" readonly>
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="canvasHeight" type="range" min="100" max="450"
                                                   id="form_height_range"
                                                   class="opacity-range range">
                                        </div>

                                        <!--Form Width-->
                                        <div class="col-md-6 no-padding">
                                            <label>Width</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="canvasWidth" class="form-control form-opacity" readonly>
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="canvasWidth" type="range" min="250" max="760"
                                                   id="form_width_range"
                                                   class="opacity-range range">
                                        </div>

                                        <!--Form Background Color-->
                                        <div class="col-md-6 no-padding">
                                            <label>Background Color</label>
                                        </div>
                                        <div class="col-md-6 no-padding">
                                            <input type="text" id="canvas_background_color">
                                            <input type="hidden" v-model="canvas_background_color"/>
                                        </div>

                                        <!--Form Opacity-->
                                        <div class="col-md-6 form-h pull-left no-padding vertical-m">
                                            <label>Form Opacity</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="canvasOpacity" class="form-control form-opacity">
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="canvasOpacity" type="range" class="opacity-range range"
                                                   min="0" max="100">
                                        </div>


                                    </div>

                                    <hr class="hr-breaker">

                                    <!--Add New Page-->
                                    <div class="col-sm-12 form-h opacity-range">
                                        <button class="btn btn-add-page">Add Page</button>
                                    </div>

                                </div>
                            </div>

                            <!--Submit Button Settings-->
                            <div v-show="isEqual('2buttons')">
                                <div class="wrapper-sidebar">

                                    <h5>SUBMIT BUTTON</h5>
                                    <div class="row">

                                        <!--Button Image-->
                                        <div class="col-md-6 no-padding">
                                            <label>Button Image</label>
                                        </div>
                                        <div class="col-md-4 no-padding">
                                            <ul class="list-inline upload-list">
                                                <li class="fileUpload upload-btn">
                                                    <center><span class="icon icon-image-upload"></span></center>
                                                    <input type="file" class="upload"/>
                                                </li>
                                            </ul>
                                        </div>
                                        <div class="col-md-2 no-padding upload-list">
                                            <a href="#"><span class="pull-right icon-trash"></span> </a>
                                        </div>

                                        <!--Button Opacity-->
                                        <div class="col-md-6 form-h pull-left no-padding vertical-m">
                                            <label>Opacity</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="buttonOpacity" class="form-control form-opacity">
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="buttonOpacity" type="range" class="opacity-range range"
                                                   min="0" max="100">
                                        </div>

                                        <!--Submit Button Color-->
                                        <div class="col-md-6 no-padding">
                                            <label>Background Color</label>
                                        </div>
                                        <div class="col-md-6 no-padding">
                                            <input type="text" id="submit_color">
                                            <input type="hidden" v-model="submit_color"/>
                                        </div>

                                        <!--Submit Text Color-->
                                        <div class="thead col-md-6 no-padding">
                                            <label>Text Color</label>
                                        </div>
                                        <div class="thead col-md-6 no-padding">
                                            <input type="text" id="submit_text_color">
                                            <input type="hidden" v-model="submit_text_color"/>
                                        </div>

                                        <!--Submit Button Text-->
                                        <div class="col-md-6 no-padding">
                                            <label>Submit Button Text</label>
                                        </div>
                                        <div class="col-md-6 no-padding form-h">
                                            <input type="text" id="submit-text"
                                                   v-model="submit_text"
                                                   class="form-control">
                                        </div>

                                        <!--Font Size-->
                                        <div class="col-md-6 form-h pull-left no-padding vertical-m">
                                            <label>Font Size</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="button_text_size" class="form-control form-opacity">
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="button_text_size" type="range" class="opacity-range range"
                                                   min="14" max="25">
                                        </div>

                                        <!--Font Family-->
                                        <div class=" col-md-6 no-padding">
                                            <label>Font family</label>
                                        </div>
                                        <div class="col-md-6 no-padding">
                                            <select class="dropdown-toggle" v-model="button_font_family">
                                                <option v-for="ffamily in fontFamilyList" :value="ffamily">
                                                    {{ffamily}}
                                                </option>
                                            </select>
                                        </div>

                                    </div>
                                </div>
                            </div>

                            <!--Field Values Settings-->
                            <div v-show="isEqual('2fieldsettings')">
                                <div class="wrapper-sidebar">

                                    <!--SELECTED FIELD INDICATOR-->
                                    <h5 class="field-selected">{{selected}} - SELECTED</h5>

                                    <!--APPLY TO ALL SETTINGS-->
                                    <div class="row">
                                        <label class="checkbox-inline">
                                            <input type="checkbox" v-model="applyToAll">APPLY TO ALL
                                        </label>
                                    </div>
                                    <hr>
                                    <h5>INPUT OPTION</h5>

                                    <!--Font Size-->
                                    <div class="row">
                                        <div class="col-md-6 no-padding">
                                            <label>Font size</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="fieldFontSize" id="button_fontsize_text"
                                                   class="form-control form-opacity" readonly>
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="fieldFontSize" type="range" min="12" max="36"
                                                   id="button_fontsize_range"
                                                   class="opacity-range range">
                                        </div>
                                    </div>

                                    <!--Font Family-->
                                    <div class="row">
                                        <div class=" col-md-6 no-padding">
                                            <label>Font family</label>
                                        </div>
                                        <div class="col-md-6 no-padding form-h">
                                            <select class="dropdown-toggle" v-model="field_font_family">
                                                <option v-for="ffamily in fontFamilyList" :value="ffamily">{{ffamily}}
                                                </option>
                                            </select>
                                        </div>
                                    </div>

                                    <!--Font Color-->
                                    <div class="row">
                                        <div class="col-md-6 no-padding">
                                            <label>Font Color</label>
                                        </div>
                                        <div class="col-md-6 no-padding">
                                            <input type="text" id="field_text_color">
                                            <input type="hidden" v-model="field_text_color"/>
                                        </div>
                                    </div>

                                    <!--Field Width-->
                                    <div class="row">
                                        <div class=" col-md-6 no-padding">
                                            <label>Field Width</label>
                                        </div>
                                        <div class="col-md-6 no-padding ">
                                            <select class="dropdown-toggle" v-model="field_width">
                                                <option v-for="field in field_width_list"
                                                        :value="field.value">
                                                    {{field.display}}
                                                </option>
                                            </select>
                                        </div>
                                    </div>

                                    <!--Field Background Color-->
                                    <div class="row">
                                        <div class="col-md-6 no-padding">
                                            <label>Field Background</label>
                                        </div>
                                        <div class="col-md-6 no-padding">
                                            <input type="text" id="field_color">
                                            <input type="hidden" v-model="field_color"/>
                                        </div>
                                    </div>

                                    <!--Field Border Color-->
                                    <div class="row">
                                        <div class="col-md-6 no-padding">
                                            <label>Field Border Color</label>
                                        </div>

                                        <div class="col-md-2 no-padding no-margin">
                                            <label class="custom-checkbox">
                                                <input type="checkbox" v-model="hasFieldBorder">
                                                <span class="checkmark"></span>
                                            </label>
                                        </div>

                                        <div class="col-md-4 no-padding no-margin">
                                            <input type="text" id="field_border_color">
                                            <input type="hidden" v-model="field_border_color"/>
                                        </div>
                                    </div>

                                    <!--Field Opacity-->
                                    <div class="row">
                                        <div class="col-md-6 form-h pull-left no-padding vertical-m">
                                            <label>Field Opacity</label>
                                        </div>
                                        <div class="col-md-2 form-h opacity-range">
                                            <input v-model="field_opacity" class="form-control form-opacity">
                                        </div>
                                        <div class="col-md-4 form-h opacity-range">
                                            <input v-model="field_opacity" type="range" class="opacity-range range"
                                                   min="0" max="100">
                                        </div>
                                    </div>

                                    <!--Field Type Settings-->
                                    <div class="row">
                                        <div class=" col-md-6 no-padding">
                                            <label>Field type</label>
                                        </div>
                                        <div class="col-md-6 no-padding form-h">
                                            <select v-model="field_type" class="dropdown-toggle" id="field-type">
                                                <option v-for="type in field_type_list" :value="type">{{type}}</option>
                                            </select>
                                        </div>
                                    </div>

                                    <!--Input Label Settings-->
                                    <div v-if="field_type == 'Input Box'" class="row">
                                        <div class=" col-md-6 no-padding">
                                            <label>Input Label</label>
                                        </div>
                                        <div class="col-md-6 no-padding form-h">
                                            <select class="dropdown-toggle" v-model="input_type">
                                                <option v-for="type in input_type_list" :value="type">{{type}}</option>
                                            </select>
                                        </div>
                                    </div>

                                    <!--Label Text Size Settins-->
                                    <!--<div class="row">-->
                                        <!--<div class="col-md-6 no-padding">-->
                                            <!--<label>Label size</label>-->
                                        <!--</div>-->
                                        <!--<div class="col-md-6 no-padding form-h">-->
                                            <!--<input class="form-control">-->
                                        <!--</div>-->
                                    <!--</div>-->

                                    <!--&lt;!&ndash;Label Color Settings&ndash;&gt;-->
                                    <!--<div class="row">-->
                                        <!--<div class="col-md-6 no-padding">-->
                                            <!--<label>Label Color</label>-->
                                        <!--</div>-->
                                        <!--<div class="col-md-6 no-padding">-->
                                            <!--<input type="text" class="demo form-control" data-control="hue">-->
                                        <!--</div>-->
                                    <!--</div>-->

                                    <div v-if="field_type == 'Dropdown' || field_type == 'Checkbox' || field_type == 'Radio Button'"
                                         class="input-options" id='dropdown-div'>
                                        <span class="color-white">Field values "seperate with comma(,)"</span>
                                        <input v-model="list_values_text" type='text' size='20'
                                               style="margin: 0px !important;"/>
                                        <span v-if="list_values.length > 3" id="error-msg"
                                              style="color:red;">Maximum of 3 options.</span>
                                    </div>

                                </div>
                            </div>

                            <!--Deleted Fields container-->
                            <div v-show="isEqual('3selection')">
                                <div class="wrapper-sidebar" style="display: block;">
                                    <ul class="element-base" id="custom-field-container" style="display: inline-block;">
                                        <!--<li guestinfoid="b63ad8f2-57e1-e711-892a-6807150701e7"-->
                                        <!--id="field-b63ad8f2-57e1-e711-892a-6807150701e7"-->
                                        <!--class="element-item custom-field-draggable ui-draggable ui-draggable-handle">-->
                                        <!--<h4>Title</h4></li>-->
                                    </ul>
                                    <hr>
                                    <ul id="field-spacer" style="display: inline-block;">
                                        <li class="element-item-spacer ui-draggable ui-draggable-handle">
                                            <h4>Spacer Field</h4>
                                        </li>
                                    </ul>
                                </div>
                            </div>

                        </div>
                    </div>
                    <!-- Sidebar Main Ends -->
                </div>

            </div>
            <!-- Ipad Start -->
            <div class="col-md-9 no-padding">
                <div class="ipad-header">
                    <h5>iPad Screen View</h5>
                </div>
                <div class="ipad-screen" :style="ipad_screen">
                    <div class="logo-placeholder">
                        <center><img src="content/img/logo.png"></center>
                    </div>


                    <!--Field Holder-->
                    <vuedraggable :style="formDragger" :resizable="true" :draggable="true"
                                  :h="canvasHeight" :w="canvasWidth"
                                  :handles="['mr', 'br', 'bm']"
                                  :minw="minW" :minh="minH"
                                  :parent="true" @resizing="onResize">
                        <table :style="ipadForm">
                            <tbody>
                            <tr v-for="field in guest_fields">
                                <layout-row :id="field.field_name + '-' + field.id"
                                            :applyToAll="applyToAll"
                                            :placeholder="field.field_name"
                                            :type="field_type"
                                            :styleValues="field_data"
                                            :listvalues="list_values"
                                            :title="field.field_name"
                                            :input_type="input_type"
                                            @clicked="selectedValue"/>
                            </tr>
                            </tbody>
                        </table>

                        <!--<ul class="ipad_sortable_fields">-->
                        <!--<li v-for="field in guest_fields" class="field-element sort-field" :style="li_ipad_fields">-->
                        <!--<ul style="top: 20%; position:absolute; right: 10px;" class="list-inline span-icon no-padding no-margin">-->
                        <!--<li class="no-padding no-margin"><span class="fa fa-arrows"></span></li>-->
                        <!--</ul>-->
                        <!--<layout-row :id="field.field_name + '-' + field.id"-->
                        <!--:applyToAll="applyToAll"-->
                        <!--:placeholder="field.field_name"-->
                        <!--:styleValues="field_data"-->
                        <!--@clicked="selectedValue"/>-->
                        <!--</li>-->
                        <!--</ul>-->


                        <!--Submit Button-->
                        <div :style="submitButtonContainer">
                            <button :style="submitButtonStyle">
                                {{submit_text}}
                            </button>
                        </div>

                    </vuedraggable>
                </div>
            </div>
        </div>
        <center>
            <ul class="list-inline">
                <li>
                    <button class="btn btn-block btn-create-event btn-ignore" type="submit">
                        SAVE
                    </button>
                </li>
            </ul>
        </center>
    </div>
</template>
<style>
    @import "../../../node_modules/spectrum-colorpicker/spectrum.css";
</style>
<script type="text/babel">

    import draggable from 'vuedraggable'
    import vuedraggable from 'vue-draggable-resizable'

    import FormCell from '../../../main/js/components/form-cell.vue'
    import LayoutGroup from './layout-group.vue'
    import LayoutRow from './layout-input-row.vue'
    import spectrum from 'spectrum-colorpicker'

    import $ from 'jquery'

    export default {
        name: 'LayoutForm',
        components: {
            draggable,
            vuedraggable,
            FormCell,
            LayoutGroup,
            LayoutRow,
        },
        data() {
            return {
                field_width: '',
                field_width_list: [],
                li_ipad_fields: {
                    marginBottom: '10px',
                    paddingLeft: '5px',
                    paddingRight: '5px',
                    display: 'inline-block',
                },
                colors: '#fff',
                canvas_background_color: '#fff',
                submit_color: '#000',
                submit_text_color: '#fff',
                field_text_color: '#000',
                field_color: '#fff',
                field_border_color: '#fff',
                hasFieldBorder: true,
                field_border_width: '1px',
                field_opacity: 100,
                field_type: 'Input Box',
                field_type_list: [
                    'Input Box',
                    'Dropdown',
                    'Checkbox',
                    'Radio Button'
                ],
                input_type: 'As Placeholder',
                input_type_list: [
                    'As Label',
                    'As Placeholder'
                ],
                list_values: [],
                list_values_text: '',
                submit_text: 'SUBMIT',
                button_text_size: 14,
                button_font_family: 'Arial',
                field_font_family: 'Arial',
                fontFamilyList: [
                    'Arial',
                    'Calibri',
                    'Calisto',
                    'Cambria',
                    'Comics Sans',
                    'Constantia',
                    'Copperplate Gothic'
                ],
                fieldSizeList: [
                    {value: '25px', displayName: '1'},
                    {value: '50px', displayName: '2'},
                    {value: '75px', displayName: '3'},
                    {value: '100px', displayName: '4'},
                ],
                submitButtonContainer: {
                    margin: '15px',
                    position: 'absolute',
                    right: '0',
                    bottom: '0',
                    paddingTop: '10px',
                    padding: '0'
                },
                submitButtonStyle: {
                    width: '100px',
                    float: 'right',
                    background: 'rgba(0, 0, 0, 1)',
                    color: '#fff',
                    border: '0',
                    borderRadius: '5px',
                    padding: '10px 20px'
                },
                ipad_screen: {
                    width: '768px'
                },
                inputForm: {
                    width: '200px'
                },
                formDragger: {
                    borderRadius: '5px',
                    position: 'absolute',
                    background: 'blue',
                    opacity: '1'
                },
                ipadForm: {
                    marginTop: '20px',
                    marginLeft: '15px',
                    marginBottom: '10px',
                    width: this.canvasWidth + 'px',
                },
                fields: [],
                field_data: {
                    borderRadius: '5px',
                },
                tabs: [
                    {value: '1generalsettings', displayName: 'General Settings'},
                    {value: '2buttons', displayName: 'Buttons'},
                    {value: '2fieldsettings', displayName: 'Field Settings'},
                    {value: '3selection', displayName: 'Field Selection'},
                ],
                activeTabName: "2fieldsettings",
                guest_fields: guest_fields,
                csrf,
                canvasHeight: 100,
                canvasWidth: 500,
                canvasColor: 'red',
                canvasOpacity: 100,
                buttonOpacity: 100,
                minW: 250,
                minH: 150,
                selected: 'NOTHING',
                id: '',
                applyToAll: false,
                fieldFontSize: 12
            }
        },
        created() {


            this.canvasHeight = 0
            this.canvasWidth = 0
            let heightConst = 60

            if (this.field_type == 'Checkbox' || this.field_type == 'Radio Button' || this.input_type == 'As Label') {
                heightConst = 90
            }

            // height and width calculation
            for (const field of this.guest_fields) {
                this.canvasHeight += heightConst
                this.canvasWidth += 80
            }

            // field width init
            this.field_data.width = this.canvasWidth - 30 + 'px'
            this.field_data.fontSize = this.fieldFontSize + 'px'
            this.field_data.background = this.field_color

            //field_width_list
            let display = 1
            let dividedWidth = Math.round((this.canvasWidth - 30) / 4)
            for (var i = 1; i <= 4; i++) {
                this.field_width_list.push(
                    {
                        'display': display,
                        'value': Math.round(dividedWidth * i)
                    }
                )
                display++
            }

            // ipad form width init
            this.ipadForm = {
                marginTop: '20px',
                marginLeft: '15px',
                marginBottom: '10px',
                width: this.canvasWidth - 30 + 'px',
                height: this.canvasHeight - 80 + 'px'
            }
        },
        mounted: function () {
            var that = this
            $('#background_color').spectrum({
                color: this.colors,
                preferredFormat: "hex",
                showButtons: false,
                showAlpha: true,
                move: function (color) {
                    that.colors = color.toHexString()
                }
            })

            //canvas_background_color
            $('#canvas_background_color').spectrum({
                color: this.canvas_background_color,
                preferredFormat: "hex",
                showInput: true,
                showButtons: false,
                move: function (color) {
                    that.canvas_background_color = color.toHexString()
                }
            })

            // submit color
            $('#submit_color').spectrum({
                color: this.submit_color,
                preferredFormat: "hex",
                showInput: true,
                showButtons: false,
                move: function (color) {
                    that.submit_color = color.toHexString()
                }
            })

            //submit_text_color
            $('#submit_text_color').spectrum({
                color: this.submit_text_color,
                preferredFormat: "hex",
                showInput: true,
                showButtons: false,
                move: function (color) {
                    that.submit_text_color = color.toHexString()
                }
            })

            //field_text_color
            $('#field_text_color').spectrum({
                color: this.field_text_color,
                preferredFormat: "hex",
                showInput: true,
                showButtons: false,
                move: function (color) {
                    that.field_text_color = color.toHexString()
                }
            })

            //field_color
            $('#field_color').spectrum({
                color: this.field_color,
                preferredFormat: "hex",
                showInput: true,
                showButtons: false,
                move: function (color) {
                    that.field_color = color.toHexString()
                }
            })

            //field_border_color
            $('#field_border_color').spectrum({
                color: this.field_border_color,
                preferredFormat: "hex",
                showInput: true,
                showButtons: false,
                move: function (color) {
                    that.field_border_color = color.toHexString()
                }
            })
        },
        watch: {
            button_font_family: function (val) {
                this.button_font_family = val
                this.submitButtonStyle.fontFamily = val
            },
            button_text_size: function (val) {
                this.button_text_size = val
                this.submitButtonStyle.fontSize = val + 'px'
                this.submitButtonStyle.width = parseInt(100) + parseInt(val) + 'px'
            },
            submit_text: function (val) {
                this.submit_text = val
            },
            submit_text_color: function (val) {
                this.submitButtonStyle.color = val
                this.submit_text_color = val
            },
            submit_color: function (val) {
                this.submitButtonStyle.background = val
                this.submit_color = val
            },
            colors: function (val) {
                this.ipad_screen.background = val
                this.colors = val
            },
            canvas_background_color: function (val) {
                this.formDragger.background = val

                this.canvas_background_color = val
            },
            fieldFontSize: function (val) {
                this.fieldFontSize = val
                this.field_data.fontSize = val + 'px'
            },
            field_font_family: function (val) {
                this.field_font_family = val
                this.field_data.fontFamily = val
            },
            field_color: function (val) {
                this.field_color = val
                this.field_data.background = this.field_color
            },
            field_text_color: function (val) {
                this.field_text_color = val
                this.field_data.color = val
            },
            field_border_color: function (val) {
                this.field_border_color = val
                this.field_data.borderColor = val
            },
            hasFieldBorder: function (val) {
                this.hasFieldBorder = val
                if (val) {
                    this.field_border_width = '1px'
                    this.field_data.borderWidth = '1px'
                } else {
                    this.field_border_width = '0px'
                    this.field_data.borderWidth = '0px'
                }
            },
            field_width: function (val) {
                this.field_width = val
                this.field_data.width = val + 'px'
            },
            field_type: function (val) {
                this.field_type = val
            },
            input_type: function(val){
                this.input_type = val
            },
            list_values_text: function (val) {
                this.list_values_text = val
                this.list_values = this.list_values_text.split(',')
            },
            applyToAll: function (val) {
                this.applyToAll = val
            },
            activeTabName: function (val) {
                this.activeTabName = val
            },
            field_opacity: function (val) {
                let opacity = val / 100
                let color_opacity = this.hexToRgbA(this.field_color, opacity)
                this.field_data.background = color_opacity
                this.field_opacity = val
            },
            buttonOpacity: function (val) {
                let opacity = val / 100
                let color_opacity = this.hexToRgbA(this.submit_color, opacity)
                this.submitButtonStyle.background = color_opacity
                this.buttonOpacity = val
            },
            canvasOpacity: function (val) {
                let opacity = val / 100
                let color_opacity = this.hexToRgbA(this.canvas_background_color, opacity)
                this.formDragger.background = color_opacity
                this.canvasOpacity = val
            },
            canvasWidth: function (val) {
                this.canvasWidth = val
                this.canvasWidth = parseInt(this.canvasWidth)
                this.formDragger.width = val + 'px'
                this.ipadForm.width = this.canvasWidth - 30 + 'px'
                this.field_width = this.canvasWidth - 30

                //field_width_list
                let display = 1
                this.field_width_list = []
                let dividedWidth = Math.round((this.canvasWidth - 30) / 4)
                for (var i = 1; i <= 4; i++) {
                    this.field_width_list.push(
                        {
                            'display': display,
                            'value': Math.round(dividedWidth * i)
                        }
                    )
                    display++
                }

                let width_val = this.field_width
                this.field_data = {
                    id: this.id,
                    fontSize: this.fieldFontSize + 'px',
                    borderRadius: '5px',
                    fontFamily: this.field_font_family,
                    color: this.field_text_color,
                    width: width_val + 'px',
                    background: this.field_color,
                    borderColor: this.field_border_color,
                    borderWidth: this.field_border_width
                }

            },
            canvasHeight: function (val) {
                this.canvasHeight = val
                this.canvasHeight = parseInt(this.canvasHeight)
                this.formDragger.height = val + 'px'
            }
        },
        methods: {
            selectedValue(value, id) {
                this.selected = value
                this.id = id
            },

            onResize: function (x, y, width, height) {
                this.canvasWidth = width
                this.canvasHeight = height

                this.ipadForm = {
                    marginTop: '20px',
                    marginLeft: '15px',
                    marginBottom: '10px',
                    width: this.canvasWidth - 30 + 'px',
                }

                //field_width_list
                let display = 1
                this.field_width_list = []
                let dividedWidth = Math.round((this.canvasWidth - 30) / 4)
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
            hexToRgbA(hex, alpha) {
                var c = hex.substring(1).split('');
                if (c.length == 3) {
                    c = [c[0], c[0], c[1], c[1], c[2], c[2]];
                }
                c = '0x' + c.join('');
                return 'rgba(' + [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',') + ',' + alpha + ')';
            },
            changeColor() {
                console.log('sak;sjlajs')
            },
            updateList() {
                console.log(JSON.stringify(this.guest_fields));
            },
            isEqual(name) {
                return this.activeTabName === name
            }
        }
    }
</script>