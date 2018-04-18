<template>
    <div class="wrapper-sidebar" style="display: block;">
        <ul class="custom-field-draggable" v-for="(item, index) in removed_items" style="display: inline-block;">
            <!--     <li class="element-item ui-draggable ui-draggable-handle"> -->
            <li class="element-item custom-field-draggable ui-draggable ui-draggable-handle">
                <h4>{{item.field_name}}</h4>
            </li>
        </ul>
        <hr>
        <ul id="field-spacer" style="display: inline-block;">

            <li class="element-item-spacer ui-draggable ui-draggable-handle">
                <h4>Spacer Field</h4>
            </li>
        </ul>
    </div>
</template>
<style>
    @import '../../../node_modules/jquery-ui/themes/base/draggable.css';
</style>
<script type="text/babel">

    import draggable from '../../../node_modules/jquery-ui/ui/widgets/draggable'

    export default {
        name: 'LayoutRemoveFieldSettings',
        props: {
            removed_items: {
                type: Array
            }
        },
        created() {
            let that = this
            if (this.removed_items.length > 0) {
                this.$nextTick(function () {
                    $('.custom-field-draggable ').draggable({
                        cursor: 'move',
                        helper: "clone",
                        zIndex: 1100,
                        revert: "invalid",
                        revertDuration: 700,
                        connectToSortable: 'table tbody',
                        start: function (event, ui) {
                            that.$emit('drag', true)
                        },
                    })
                })
            }
        },
        watch: {
            removed_items: function (val) {
                var that = this
                this.$nextTick(function () {
                    $('.custom-field-draggable ').draggable({
                        helper: "clone",
                        zIndex: 1100,
                        revert: "invalid",
                        revertDuration: 700,
                        connectToSortable: 'table tbody',
                        start: function (event, ui) {
                            that.$emit('drag', true)
                        },
                    })
                })
            }
        },
        mounted: function () {
            var that = this
            $('#field-spacer').draggable({
                revertDuration: 700,
                helper: 'clone',
                connectToSortable: 'table tbody',
                start: function (event, ui) {
                    that.$emit('drag', true)
                },
            })
        }
    }
</script>