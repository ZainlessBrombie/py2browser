<template>
    <div class="wrapper">
        Stream/IO. (e.g. to a file)
        <CustomTable
                :columns="['name', 'mode', 'encoding', 'closed']"
                :headings="{name: 'Name', mode: 'Mode', encoding: 'Encoding', closed: 'Closed'}"
                :rows="[{name, mode, encoding, closed}]"
                :forceEqualLength="true">
        </CustomTable>
    </div>
</template>

<script>
    import CustomTable from "../table/CustomTable";
    export default {
        name: "StreamDisplay",
        components: {CustomTable},
        props: {
            name: {
                type: String,
                default: 'no name'
            },
            mode: {
                type: String,
                default: 'unset'
            },
            encoding: {
                type: String,
                default: 'none'
            },
            closed: {
                type: Boolean,
                default: false
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        padding: 7px;
        border-radius: 4px;
        border: 2px solid dimgrey;
        flex-grow: 1;
    }

</style>
