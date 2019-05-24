<template>
    <div>
        This object of type {{(value || {}).type}} cannot be displayed currently.<br>
        Here is what we know:<br>
        <i style="font-style: normal; font-family: 'Lucida Console', Monaco, monospace" v-for="k in Object.keys(value && value.data || {})">
            &nbsp;{{k}}: {{['number', 'string'].includes(typeof value.data[k]) ? value.data[k] : 'Object'}}<br>
        </i>
    </div>
</template>

<script>
    export default {
        name: "UnknownDisplay",
        props: {
            value: {
                type: Object,
            }
        }
    }
</script>

<style scoped>

</style>
