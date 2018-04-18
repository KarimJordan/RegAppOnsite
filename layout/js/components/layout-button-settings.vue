<template>
    <div class="wrapper-sidebar">
        <h5>SUBMIT BUTTON</h5>
        <div class="row">
            <div class="col-md-6 no-padding">
                <label>Button Image</label>
            </div>
            <div class="col-md-4 no-padding">
                <ul class="list-inline upload-list">
                    <li class="fileUpload upload-btn">
                        <form enctype="multipart/form-data" method="post">
                            <center><span class="icon icon-image-upload"></span></center>
                            <input @change="button_upload($event.target.files)" type="file" class="upload"/>
                        </form>
                        <input type="hidden" v-model="button_image_value" name="background_image"/>
                    </li>
                </ul>
            </div>
            <div class="col-md-2 no-padding upload-list">
                <a @click="hide_button"><span class="pull-right icon-trash"></span> </a>
            </div>

            <!--Button Opacity-->
            <div class="col-md-6 form-h pull-left no-padding vertical-m">
                <label>Opacity</label>
            </div>
            <div class="col-md-2 form-h opacity-range">
                <input v-model="button_opacity_value" class="form-control form-opacity">
            </div>
            <div class="col-md-4 form-h opacity-range">
                <input v-model="button_opacity_value" type="range" class="opacity-range range"
                       min="0" max="100">
            </div>

            <!--Font Size-->
            <div class="col-md-6 form-h pull-left no-padding vertical-m">
                <label>Font Size</label>
            </div>
            <div class="col-md-2 form-h opacity-range">
                <input v-model="button_font_size_value" class="form-control form-opacity">
            </div>
            <div class="col-md-4 form-h opacity-range">
                <input v-model="button_font_size_value" type="range" class="opacity-range range"
                       min="12" max="28">
            </div>

            <!--Submit Button Text-->
            <div class="col-md-6 no-padding">
                <label>Submit Button Text</label>
            </div>
            <div class="col-md-6 no-padding form-h">
                <input type="text"
                       v-model="submit_button_text_value"
                       class="form-control">
            </div>

            <!--Next Button Text-->
            <div v-if="has_second_page" class="col-md-6 no-padding">
                <label>Next Button Text</label>
            </div>
            <div v-if="has_second_page" class="col-md-6 no-padding form-h">
                <input type="text"
                       v-model="next_button_text_value"
                       class="form-control">
            </div>

            <!--Back Button Text-->
            <div v-if="has_second_page" class="col-md-6 no-padding">
                <label>Back Button Text</label>
            </div>
            <div v-if="has_second_page" class="col-md-6 no-padding form-h">
                <input type="text"
                       v-model="back_button_text_value"
                       class="form-control">
            </div>

            <!--Font Family-->
            <div class=" col-md-6 no-padding">
                <label>Font family</label>
            </div>
            <div class="col-md-6 no-padding">
                <select class="dropdown-toggle" v-model="button_font_family_value">
                    <option v-for="ffamily in fontFamilyList" :value="ffamily">
                        {{ffamily}}
                    </option>
                </select>
            </div>

            <!--Button Color-->
            <div class="col-md-6 no-padding">
                <label>Background Color</label>
            </div>
            <div class="col-md-6 no-padding">
                <input type="text" id="button_color">
                <input type="hidden" v-model="button_color_value"/>
            </div>

            <!--Button Text Color-->
            <div class="thead col-md-6 no-padding">
                <label>Text Color</label>
            </div>
            <div class="thead col-md-6 no-padding">
                <input type="text" id="button_text_color">
                <input type="hidden" v-model="button_text_color_value"/>
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
        name: 'LayoutButtonSettings',
        props: {
            button_opacity: {
                type: String
            },
            button_color: {
                type: String
            },
            button_text_color: {
                type: String
            },
            button_font_size: {
                type: String
            },
            button_font_family: {
                type: String
            },
            submit_button_text: {
                type: String
            },
            next_button_text: {
                type: String
            },
            back_button_text: {
                type: String
            },
            has_second_page: {
                type: Boolean
            }
        },
        data() {
            return {
                button_opacity_value: '',
                button_color_value: '',
                button_text_color_value: '',
                button_font_size_value: '',
                button_font_family_value: '',
                submit_button_text_value: '',
                next_button_text_value: '',
                back_button_text_value: '',
                button_image_value: '',
                fontFamilyList: [
                    'Arial',
                    'Calibri',
                    'Calisto',
                    'Cambria',
                    'Comics Sans',
                    'Constantia',
                    'Copperplate Gothic'
                ],
            }
        },
        created() {
            this.button_opacity_value = this.button_opacity
            this.button_color_value = this.button_color
            this.button_font_size_value = this.button_font_size
            this.button_font_family_value = this.button_font_family
            this.submit_button_text_value = this.submit_button_text
            this.next_button_text_value = this.next_button_text
            this.back_button_text_value = this.back_button_text
            this.button_text_color_value = this.button_text_color
        },
        watch: {
            button_opacity_value: function (val) {
                this.$emit('button_opacity', val)
                this.button_opacity_value = val
            },
            button_color_value: function (val) {
                this.$emit('button_color', val)
                this.button_color_value = val
            },
            button_text_color_value: function (val) {
                this.$emit('button_text_color', val)
                this.button_text_color_value = val
            },
            button_font_size_value: function (val) {
                this.$emit('button_font_size', val)
                this.button_font_size_value = val
            },
            button_font_family_value: function (val) {
                this.$emit('button_font_family', val)
                this.button_font_family_value = val
            },
            submit_button_text_value: function (val) {
                this.$emit('submit_button_text', val)
                this.submit_button_text_value = val
            },
            next_button_text_value: function (val) {
                this.$emit('next_button_text', val)
                this.next_button_text_value = val
            },
            back_button_text_value: function (val) {
                this.$emit('back_button_text', val)
                this.back_button_text_value = val
            }
        },
        mounted: function () {
            //button color
            var that = this
            $('#button_color').spectrum({
                color: this.button_color_value,
                preferredFormat: "hex",
                showButtons: false,
                move: function (color) {
                    that.button_color_value = color.toHexString()
                }
            })

            //button_text_color
            $('#button_text_color').spectrum({
                color: this.button_text_color_value,
                preferredFormat: "hex",
                showButtons: false,
                move: function (color) {
                    that.button_text_color_value = color.toHexString()
                }
            })
        },
        methods: {
            hide_button(){
                this.$emit('hide_button')
            },
            button_upload(file) {
                let that = this
                let fileData = file[0]
                let fileReader = new FileReader()
                fileReader.readAsDataURL(fileData)
                fileReader.onload = function (e) {
                    console.log(that.button_image_value)
                    let outputFile = e.target.result
                    that.button_image_value = outputFile
                    that.$emit('button', that.button_image_value)
                }

            },
        }
    }
</script>