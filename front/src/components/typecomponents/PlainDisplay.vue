<template>
    <div class="wrapper">
        &nbsp;<i class="code" :style="{color}">{{value}}</i>
    </div>
</template>

<script>
    export default {
        name: "NumberDisplay",
        props: {
            value: {
                type: String,
                default: '',
            },
            color: {
                type: String,
                default: 'black'
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
