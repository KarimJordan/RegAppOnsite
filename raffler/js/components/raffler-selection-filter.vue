<template>
    <tbody>
    <!--<tr>-->
    <!--{{selection_filter}}-->
    <!--</tr>-->
    <tr v-for="filter, index in selection_filter">
        <td>
            <select name="" class="form-control" v-model="filter.selected_filter">
                <option v-for="filter in filters" :value="filter">{{filter}}</option>
            </select>
        </td>
        <td>
            <!--insert list based on fields-->
            <select @change="get_values(index, filter.selected_field)" name="" class="form-control"
                    v-model="filter.selected_field">
                <option value="All">All</option>
                <option v-for="field in guest_fields" :value="field.field_name">
                    {{field.field_name}}
                </option>
            </select>
        </td>
        <td><label class="lbl-center">WITH</label></td>
        <td>
            <!--Values of the field selected-->
            <select name="" class="form-control" v-model="filter.selected_value">
                <option value="All">All</option>
                <option v-for="info in selection_filter[index].field_values" :value="info.value">{{info.value}}</option>
            </select>
        </td>
        <td>
            <button @click="remove_filter(index)" type="button" class="btn btn-danger remove"><i
                    class="glyphicon glyphicon-remove-sign"></i> &nbsp;
            </button>
        </td>
    </tr>
    </tbody>
</template>
<script type="text/babel">

    import axios from 'axios'

    export default {
        name: 'RafflerSelectionFilter',
        data() {
            return {
                selected_filter: 'Include',
                selected_field: 'All',
                selected_info: 'All',
                filters: [
                    'Include', 'Include Specific', 'Exclude', 'Exclude Specific'
                ],
                guest_info_data: []
            }
        },
        props: {
            selection_filter: {
                type: Array,
                required: true
            },
            guest_fields: {
                type: Array,
                required: true
            }
        },
        methods: {
            get_values(index, value) {
//                console.log(index + ';' + value)
                let that = this
                let params = {
                    selected_field: value
                }
                let url = 'api/field_value_list/'
                params = {params: params}
                axios.get(url, params).then((response) => {
                    that.selection_filter[index].field_values = response.data.guest_infos
                })
            },
            remove_filter(index) {
                this.$emit('remove', index)
            }
        }
    }
</script>