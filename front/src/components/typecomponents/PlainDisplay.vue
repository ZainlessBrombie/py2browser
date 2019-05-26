<template>
    <div class="wrapper">
        <b v-if="heading">{{heading}}</b>
        <br v-if="heading">
        &nbsp;<i class="code" :style="{color}">{{value}}</i>
    </div>
</template>

<script>
    export default {
        name: "PlainDisplay",
        props: {
            value: {
                type: String,
                default: '',
            },
            color: {
                type: String,
                default: 'black'
            },
            heading: {
                type: String,
                default: undefined
            }
        }
    }
</script>

<style scoped>
    .wrapper {
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
