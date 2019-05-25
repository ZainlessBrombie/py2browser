<template>
    <div class="wrapper"><!-- now that I think about it I should have build this with flex... oh well -->
        <div class="line"></div>
        <div style="height: 0; margin: 0 auto; width: fit-content;">
            <div class="offset">
                <div :style="{'background-color': backgroundColor}" class="back-pane">
                    <i style="font-style: normal">{{text}}</i>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CustomDivider",
        props: {
            text: {
                type: String,
                default: undefined
            },
            backgroundColor: {
                type: String,
                default: '#ffffff'
            }
        }
    }
</script>

<style scoped>
    .wrapper {
        margin-top: 3px;
        margin-bottom: 3px;
        padding-top: 1em;
        padding-bottom: 1em;
        width: 100%;
    }

    .line {
        height: 0;
        width: 94%;
        margin-left: 3%;
        margin-right: 3%;
        border-bottom: .1em solid black;
        border-top: .1em solid black;
    }

    .offset {
        font-style: normal;
        position: relative;
        top: -1.05em;
    }

    .back-pane {
        height: 2em;
        box-sizing: border-box;
        padding-top: .4em;
        padding-left: 5px;
        padding-right: 5px;
    }
</style>
