<template>
    <div class="wrapper">
        <b>Data Series (pandas)</b>
        <div v-if="path.length">
            (<i style="font-style: normal; color: blue; cursor: pointer" v-on:click="$emit('select', path)">View Fullscreen</i>)
        </div>
        <br> <!-- todo search with server side integration -->
        Length: <i class="code">{{length}}</i>
        <br>
        dtype: <i class="code">{{dType}}</i>
        <div class="entry" v-for="(entry, index) in head.slice(0,show)">
            <div style="font-family: 'Lucida Console', Monaco, monospace">&nbsp;{{index}}:&nbsp;</div>
            <div v-if="SimpleToString.eligible(entry)" :style="SimpleToString.toSimpleString(entry).style">
                {{SimpleToString.toSimpleString(entry).value}}
            </div>
            <component v-on:select="evt => $emit('select', evt)" v-else-if="path.length < 5"
                       :is="TypeRegistry.obtain(entry, [...path, index]).component"
                       v-bind="TypeRegistry.obtain(entry, [...path, index]).props(entry)"></component>
            <div v-else><i>Hidden.</i>&nbsp;<i style="text-decoration: none; color: blue; cursor: pointer"
                                               v-on:click="() => display(index)">Jump</i></div>
        </div><!-- TODO: index numbers prepended whitespace, search -->
        <p v-on:click="expand" v-if="show < head.length">&nbsp;&nbsp;<i style="cursor: pointer">More...</i></p>
        <i v-else-if="head.length < length" style="font-style: normal; cursor: pointer">Load More From Python
            (TODO)</i><!-- TODO -->
    </div>
</template>

<script>
    import CustomTable from "../table/CustomTable";
    import SimpleToString from "./SimpleToString";

    export default {
        name: "PandasSeriesDisplay",
        components: {CustomTable},
        props: {
            path: {
                type: Array
            },
            length: {
                type: Number,
                default: 0
            },
            id: {
                type: Number,
                default: 0
            },
            head: {
                type: Array,
                default: () => []
            },
            dType: {
                type: String,
                default: 'missing'
            }
        },
        data() {
            return {
                SimpleToString,
                show: this.path.length ? 4 : 50
            }
        },
        methods: {
            display(index) {
                this.$emit('select', [...this.path, index]);
            },
            expand() {
                this.show += 50;
            },
        }
    }
</script>

<style scoped>
    .code {
        font-family: "Lucida Console", Monaco, monospace;
        font-style: normal;
    }

    .entry {
        display: flex;
        flex-direction: row;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .wrapper {
        padding: 7px;
        border-radius: 4px;
        border: 2px solid dimgrey;
        flex-grow: 1;
    }
</style>
