<template>
    <div class="wrapper">
        {{toStr}}:
        <table style="border: 1px solid black; border-collapse: collapse; margin-top: 10px">
            <tr>
                <td>module</td>
                <td>file</td>
                <td>arg count</td>
            </tr>
            <tr>
                <td class="code">{{module}}</td>
                <td>{{filename}}</td>
                <td>{{argCount}}</td>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        name: "FunctionDisplay",
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
