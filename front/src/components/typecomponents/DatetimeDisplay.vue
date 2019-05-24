<template>
    <div class="wrapper">
        &nbsp;<i class="code" style="color: blue;">{{value}}</i><i style="font-style: normal">&nbsp;({{subtype}})</i>
    </div>
</template>

<script>
    export default {
        name: "DatetimeDisplay",
        props: {
            value: {
                type: String,
                default: ''
            },
            subtype: {
                type: String,
                default: '',
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        height: 1.2em;
        overflow: hidden;
        padding: 7px;
        width: 90%;
        border-radius: 5px;
        border: 2px solid dimgrey;
    }

    .code {
        font-family: "Lucida Console", Monaco, monospace;
        font-style: normal;
    }
</style>
