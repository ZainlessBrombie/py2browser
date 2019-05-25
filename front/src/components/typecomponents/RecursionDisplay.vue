<template>
    <div>
        <i>Recursion to self {{Math.abs(depth)}} references up.</i>&nbsp;<i style="text-decoration: none; color: blue; cursor: pointer;"
    v-on:click="$emit('select', path.slice(0, path.length - Math.abs(depth)))">Jump</i>
    </div>
</template>

<script>
    export default {
        name: "RecursionDisplay",
        props: {
            path: {
                type: Array,
            },
            depth: {
                type: Number,
                default: 0,
            }
        }
    }
</script>

<style scoped>

</style>
