<template>
    <div class="wrapper">
        <b>{{subtypeStringMapping[subtype] || 'Collection'}} {{value.length ? `<${determineType(value).join(', ')}>` : '(Empty)'}}</b>
        <div class="entry" v-for="(entry, index) in value.slice(0,show)">
            <div style="font-family: 'Lucida Console', Monaco, monospace">&nbsp;{{index}}:&nbsp;</div>
            <div v-if="SimpleToString.eligible(entry)" :style="SimpleToString.toSimpleString(entry).style">
                {{SimpleToString.toSimpleString(entry).value}}
            </div>
            <component v-on:select="evt => $emit('select', evt)" v-else-if="path.length < 5" :is="TypeRegistry.obtain(entry, [...path, index]).component" v-bind="TypeRegistry.obtain(entry, [...path, index]).props(entry)"></component>
            <div v-else><i>Hidden.</i>&nbsp;<i style="text-decoration: none; color: blue; cursor: pointer" v-on:click="() => display(index)">Jump</i></div>
        </div>
        <p v-on:click="expand" v-if="show < value.length">&nbsp;&nbsp;<i style="cursor: pointer">More...</i></p>
    </div> <!-- TODO numbers should have prepended zeroes or whitespaces for consistent spacing. also: search -->
</template>

<script>
    import SimpleToString from './SimpleToString';
    import TypeRegistry from "./TypeRegistry";

    export default {
        name: "ArrayDisplay",
        props: {
            value: {
                type: Array,
                default: () => [],
            },
            subtype: {
                type: String,
                default: ''
            },
            path: {
                type: Array
            },
            typeOverride: {
                type: String,
                default: undefined
            }
        },
        data: () => ({
            SimpleToString,
            TypeRegistry,
            subtypeStringMapping: {
                list: 'List',
                set: 'Set',
                tuple: 'Tuple',
                pandas_series: 'Series (Pandas)' // deprecated
            },
            show: 50, // consider showing 50 only at first level
        }),
        methods: {
            display(index) {
                this.$emit('select', [...this.path, index]);
            },
            expand() {
                this.show += 50;
            },
            determineType(value) {
                if (this.typeOverride) return [this.typeOverride];
                const ret = [...new Set(value.map(val => val.type))];
                return ret.length > 3 ? ['mixed'] : ret;
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

    .entry {
        display: flex;
        flex-direction: row;
        margin-top: 10px;
        margin-bottom: 10px;
    }
</style>
