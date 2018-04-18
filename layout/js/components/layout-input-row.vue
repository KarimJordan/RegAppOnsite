<template>
    <div>
        <!--<div v-if="title != ''" @click="selected(title, id)">-->
        <!--<label class="checkbox-inline">{{title}}-->
        <!--<input :id="id"/>-->
        <!--</label>-->
        <!--</div>-->

        <!--<div v-if="placeholder != ''" >-->
        <!--<input :id="id"-->
        <!--:placeholder="placeholder"-->
        <!--@click="selected(placeholder, id)"-->
        <!--:style="getStyle(id)" readonly>-->
        <!--</div>-->
        <div v-if="type == 'Input Box' && input_type == 'As Placeholder'">
            <input :id="id"
                   :placeholder="placeholder"
                   @click="selected(placeholder, id)"
                   :style="getStyle(id)" readonly>
        </div>

        <div v-if="type == 'Input Box' && input_type == 'As Label'">
            <label slass="checkbox-inline" style="padding-left: 0; margin-bottom: 10px;">
                {{placeholder}}
            <input :id="id"
                   @click="selected(placeholder, id)"
                   :style="getStyle(id)" readonly>
            </label>
        </div>

        <div v-if="type == 'Dropdown'">
            <select :id="id" :style="getStyle(id)">
                <option v-for="list in listvalues" :value="list">{{list}}</option>
            </select>
        </div>

        <div v-if="type == 'Checkbox'">
            <label style="color: #fff; width: 100%;">
                {{title}}
            </label>
            <div v-for="list in listvalues">
                <div class="field-element" style="width: 100px; display: block;">
                    <div class="checkbox">
                        <input type="checkbox">
                        <label>{{list}}</label>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="type == 'Radio Button'">
            <label style="color: #fff; width: 100%;">
                {{title}}
            </label>
            <div v-for="list in listvalues">
                <div class="field-element" style="width: 100px; display: block;">
                    <div class="checkbox" >
                        <input type="radio">
                        <label>{{list}}</label>
                    </div>
                </div>
            </div>
        </div>


    </div>
</template>
<script type="text/babel">
    export default {
        name: 'LayoutInputRow',
        props: {
            placeholder: {
                type: String,
                default: ''
            },
            title: {
                type: String,
                default: ''
            },
            type: {
                type: String
            },
            input_type: {
                type: String
            },
            id: {
                type: String
            },
            applyToAll: {
                type: Boolean
            },
            title: {
                type: String
            },
            title_color: {
                type: String
            },
            title_font_size: {
                type: String
            },
            listvalues: {
                type: Array
            },
            styleValues: {
                type: Object
            }
        },
        methods: {
            selected(value, id) {
                this.$emit('clicked', value, id)
            },
            getStyle(id) {
//                console.log(this.styleValues)
                return this.styleValues
//                if (id == this.styleValues.id) {
//                    return this.styleValues
//                } else if (this.applyToAll) {
//                    return this.styleValues
//                }
            }
        }
    }
</script>