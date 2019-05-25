<template>
    <div class="wrapper">
        {{toStr}}:
        <CustomTable
                :columns="['module', 'file', 'argCount']"
                :headings="{module: 'Module', file: 'File', argCount: 'Argument Count'}"
                :rows="[{module, file: filename, argCount}]"
                :force-equal-length="true"
                style="margin-top: 10px;"
        >
        </CustomTable>
    </div>
</template>

<script>
    import CustomTable from "../table/CustomTable";
    export default {
        name: "FunctionDisplay",
        components: {CustomTable},
        props: {
            module: {
                type: String,
                default: ''
            },
            filename: {
                type: String,
                default: ''
            },
            argCount: {
                type: Number,
                default: -1
            },
            toStr: {
                type: String,
                default: ''
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        padding: 7px;
        border-radius: 4px;
        border: 2px solid dimgrey;
    }

    .code {
        font-family: "Lucida Console", Monaco, monospace;
        font-style: normal;
    }

    td {
        height: 2em;
        border: 1px solid black;
        padding: 0 1em 0 1em;
    }
    tr {
        border: 1px solid black;
    }
</style>
