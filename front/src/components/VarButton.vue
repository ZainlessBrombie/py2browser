<template>
    <div class="wrapper">
        <div v-if="markerColor || backgroundColor" :style="{'flex-grow': 1, 'background-color': markerColor, 'flex-basis': '15%'}">
        </div>
        <div style="flex-grow: 1; flex-basis: 85%; padding: .4em 0">
            <i style="font-style: normal; font-size: 1.1em;">{{name}}</i>
            <br>
            <i style="font-style: normal; font-size: .98em; color: grey">({{subtype || type}})</i>
        </div>
    </div>
</template>

<script>
    export default {
        name: "VarButton",
        props: {
            name: {
                type: String,
                default: ''
            },
            type: {
                type: String,
                default: ''
            },
            subtype: {
                type: String,
                default: undefined
            },
            backgroundColor: {
                type: String,
                default: undefined,
            },
            markerColor: {
                type: String,
                default: undefined,
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        margin: 15px 20px;
        text-align: center;
        background: white;
        border: 2px solid black;
        flex-direction: row;
        display: flex;
    }
</style>
