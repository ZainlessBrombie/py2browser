<template>
    <div class="wrapper">
        <b>Module <u>{{name}}</u></b>
        <br>
        <i style="font-style: normal" class="code">{{moduleToString}}</i>
        <br>
        <i>That's all we know.</i>
    </div>
</template>

<script>
    export default {
        name: "ModuleDisplay",
        props: {
            name: {
                type: String,
                default: undefined
            },
            moduleToString: {
                type: String,
                default: '...'
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

    .code {
        font-family: "Lucida Console", Monaco, monospace;
        font-style: normal;
    }
</style>
