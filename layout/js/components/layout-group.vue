<template>

</template>
<script type="text/babel">

    import LayoutRow from './layout-input-row.vue'

    export default {
        name: 'LayoutGroup',
        components: {
            LayoutRow
        },
        props: {
            items: {type: Array, required: true}
        }
    }
</script>