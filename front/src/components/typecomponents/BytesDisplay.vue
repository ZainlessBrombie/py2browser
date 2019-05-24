<template>
    <div class="wrapper">
        Byte array of length {{len}}.&nbsp;<i style="font-style: normal; color: blue; cursor:pointer;" v-on:click="doCopy">Copy base64 to clipboard</i>
    </div>
</template>

<script>
    export default {
        name: "BytesDisplay",
        props: {
            len: {
                type: Number,
                default: -1
            },
            value: {
                type: String,
                default: 'MISSING'
            }
        },
        methods: {
            doCopy() {
                const tag = document.createElement('input');
                document.body.append(tag);
                tag.value = this.value;
                tag.select();
                document.execCommand('copy');
                document.body.removeChild(tag);
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
</style>
