<template>
    <div class="wrapper-sidebar">
        <h5>Layout Name</h5>
        <div class="row">
            <div class="col-sm-12 form-h opacity-range">
                <input type="text" v-model="layout_name_value" required>
            </div>
        </div>
        <hr class="hr-breaker">
        <h5>Canvas</h5>
        <div class="row">
            <div class="col-md-6 no-padding">
                <label>Logo Image</label>
            </div>

            <div class="col-md-4 no-padding">
                <ul class="list-inline upload-list">
                    <li class="fileUpload upload-btn">
                        <form enctype="multipart/form-data" method="post">
                            <center><span class="icon icon-image-upload"></span></center>
                            <input @change="logo_upload($event.target.files)" type="file" class="upload"
                                   accept="image/*"/>
                        </form>
                        <input type="hidden" v-model="logo_image_value" name="background_image"/>
                    </li>
                </ul>
            </div>

            <div class="col-md-2 no-padding upload-list">
                <a @click="hide_logo"><span class="pull-right icon-trash"></span> </a>
            </div>

            <br>
            <br>

            <div class="col-md-6 no-padding ">
                <label>Background Image</label>
            </div>
            <div class="col-md-4 no-padding">
                <ul class="list-inline upload-list">
                    <li class="fileUpload upload-btn">
                        <form enctype="multipart/form-data" method="post">
                            <center><span class="icon icon-image-upload"></span></center>
                            <input @change="background_upload($event.target.files)" type="file" class="upload"/>
                        </form>
                        <input type="hidden" v-model="background_image_value" name="background_image"/>
                    </li>

                </ul>
            </div>

            <div class="col-md-2 no-padding upload-list">
                <a @click="hide_background"><span class="pull-right icon-trash"></span> </a>
            </div>

            <div class="thead col-md-6 no-padding">
                <label>Background Color</label>
            </div>

            <div class="thead col-md-6 no-padding">
                <input type="hidden" v-model="bg_color"/>
                <input type="text" id="bg_color">
            </div>
        </div>

        <hr class="hr-breaker">
        <h5>FORM</h5>
        <div class="row">
            <div class="col-md-6 no-padding">
                <label>Height</label>
            </div>
            <div class="col-md-2 form-h opacity-range">
                <input v-model="canvas_height_value" class="form-control form-opacity" readonly>
            </div>
            <div class="col-md-4 form-h opacity-range">
                <input v-model="canvas_height_value" type="range" min="100" max="450"
                       id="form_height_range"
                       class="opacity-range range">
            </div>

            <div class="col-md-6 no-padding">
                <label>Width</label>
            </div>

            <div class="col-md-2 form-h opacity-range">
                <input v-model="canvas_width_value" class="form-control form-opacity" readonly>
            </div>
            <div class="col-md-4 form-h opacity-range">
                <input v-model="canvas_width_value" type="range" min="250" max="760"
                       id="form_width_range"
                       class="opacity-range range">
            </div>

            <div class="col-md-6 no-padding">
                <label>Form Opacity</label>
            </div>
            <div class="col-md-2 form-h opacity-range">
                <input v-model="canvas_opacity_value" class="form-control form-opacity">
            </div>
            <div class="col-md-4 form-h opacity-range">
                <input v-model="canvas_opacity_value" type="range" class="opacity-range range"
                       min="0" max="100">
            </div>

            <div class="col-md-6 no-padding">
                <label>Canvas Color</label>
            </div>
            <div class="thead col-md-6 no-padding">
                <input type="hidden" v-model="canvas_color_value"/>
                <input type="text" id="canvas_color">
            </div>

        </div>
        <hr class="hr-breaker">

        <div class="col-sm-12 form-h opacity-range">
            <button @click="add_page" class="btn btn-add-page">Add Page</button>
        </div>
    </div>
</template>
<style>
    @import "../../../node_modules/spectrum-colorpicker/spectrum.css";

    #backgroundimage {
        height: auto;
        left: 0;
        margin: 0;
        min-height: 100%;
        min-width: 674px;
        padding: 0;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: -1;
    }

</style>
<script type="text/babel">

    import spectrum from 'spectrum-colorpicker'

    import $ from 'jquery'

    export default {
        name: 'LayoutGeneralSettings',
        props: {
            layout_name: {
                type: String
            },
            background_color: {
                type: String
            },
            canvas_height: {
                type: String
            },
            canvas_width: {
                type: String
            },
            canvas_color: {
                type: String
            },
            canvas_opacity: {
                type: String
            }
        },
        data() {
            return {
                bg_color: '',
                canvas_height_value: '',
                canvas_width_value: '',
                canvas_color_value: '',
                canvas_opacity_value: '',
                layout_name_value: '',
                logo_image_value: '',
                background_image_value: ''
            }
        },
        created() {
            this.layout_name_value = this.layout_name
            this.canvas_height_value = this.canvas_height
            this.canvas_width_value = this.canvas_width
            this.bg_color = this.background_color
            this.canvas_color_value = this.canvas_color
            this.canvas_opacity_value = this.canvas_opacity
        },
        watch: {
            layout_name_value: function (val) {
                this.$emit('layout_name', val)
                this.layout_name_value = val
            },
            canvas_height: function (val) {
                this.canvas_height_value = val
            },
            canvas_width: function (val) {
                this.canvas_width_value = val
            },
            canvas_height_value: function (val) {
                this.$emit('canvas_height', val)
                this.canvas_height_value = val
            },
            canvas_width_value: function (val) {
                this.$emit('canvas_width', val)
                this.canvas_width_value = val
            },
            canvas_opacity_value: function (val) {
                this.$emit('canvas_opacity', val)
                this.canvas_opacity_value = val
            },
            bg_color: function (val) {
                this.$emit('background_color', val)
                this.bg_color = val
            },
            canvas_color_value: function (val) {
                this.$emit('canvas_color', val)
                this.canvas_color_value = val
            }
        },
        mounted: function () {
            //background color
            var that = this
            $('#bg_color').spectrum({
                color: this.bg_color,
                preferredFormat: "hex",
                showButtons: false,
                showInput: true,
                move: function (color) {
                    that.bg_color = color.toHexString()
                }
            })

            $('#canvas_color').spectrum({
                color: this.canvas_color_value,
                preferredFormat: "hex",
                showButtons: false,
                showInput: true,
                move: function (color) {
                    that.canvas_color_value = color.toHexString()
                }
            })
        },
        methods: {
            hide_logo() {
                this.$emit('hide_logo')
            },
            hide_background() {
                this.$emit('hide_background')
            },
            add_page() {
                this.$emit('add_page')
            },
            logo_upload(file) {
                let that = this
                let fileData = file[0]
                let fileReader = new FileReader()
                fileReader.readAsDataURL(fileData)
                fileReader.onload = function (e) {
                    console.log(that.logo_image_value)
                    let outputFile = e.target.result
                    that.logo_image_value = outputFile
                    that.$emit('logo', that.logo_image_value)
                }

            },
            background_upload(file) {
                let that = this
                let fileData = file[0]
                let fileReader = new FileReader()
                fileReader.readAsDataURL(fileData)
                fileReader.onload = function (e) {
                    let outputFile = e.target.result
                    that.background_image_value = outputFile
                    that.$emit('background', that.background_image_value)
                }
            }
        }
    }
</script>