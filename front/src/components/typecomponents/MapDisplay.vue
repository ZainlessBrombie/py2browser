<template>
    <div class="wrapper">
        <b>{{subtypeStringMapping[subtype] || 'Map'}}
            {{value.length ? `<${determineKeyTypes(value)},${determineEntryTypes(value)}>` : '(empty)'}}</b>
        <CustomTable class="table" :columns="header" :rows="entries" :headings="tableOptions.headings">
            <div slot="keyValue" slot-scope="locals">
                <div v-if="locals.row.keyString" :style="locals.row.keyStyle">{{locals.row.keyString}}</div>
                <component
                        v-else-if="path.length < 6"
                        :is="TypeRegistry.obtain(locals.row.keyValue, [...path, [locals.row.index, 'key']]).component"
                        v-bind="TypeRegistry.obtain(locals.row.keyValue, [...path, [locals.row.index, 'key']]).props(locals.row.keyValue)"
                        v-on:select="evt => $emit('select', evt)">
                </component>
                <div v-else>
                    <i>Hidden.</i> <i class="link" v-on:click="() => display([locals.index, 'key'])">Jump</i>
                </div>
            </div>
            <div slot="valueValue" slot-scope="locals">
                <div v-if="locals.row.valueString" :style="locals.row.valueStyle">{{locals.row.valueString}}</div>
                <component
                    v-else-if="path.length < 6 && !dictDepthExceeded()"
                    :is="TypeRegistry.obtain(locals.row.valueValue, [...path, [locals.row.index, 'value']]).component"
                    v-bind="TypeRegistry.obtain(locals.row.valueValue, [...path, [locals.row.index, 'value']]).props(locals.row.valueValue)"
                    v-on:select="evt => $emit('select', evt)">
                </component>
                <div v-else>
                    <i>Hidden.</i> <i class="link" v-on:click="() => display([locals.index, 'value'])">Jump</i>
                </div>
            </div>
        </CustomTable>
    </div>
</template>

<script>
    import SimpleToString from "./SimpleToString";
    import TypeRegistry from "./TypeRegistry";
    import CustomTable from "../table/CustomTable";

    export default {
        name: "MapDisplay",
        components: {CustomTable},
        props: {
            value: {
                type: Array,
                default: () => [],
            },
            subtype: {
                type: String,
                default: 'unknown'
            },
            path: {
                type: Array
            }
        },
        data() {
            const longest = this.longestLengths('key');
            const longestValue = this.longestLengths('value');
            return ({
                TypeRegistry,
                subtypeStringMapping: {
                    dict: 'dict',
                    ordered_dict: 'OrderedDictionary'
                },
                header: ['keyValue', 'valueValue'],
                entries: this.value.map(({key, value}, index) => ({
                    keyValue: key,
                    valueValue: value,
                    keyString: key.type === 'number' ? this.toLen(key, longest) + '(' + key.data.subtype + ')' : (SimpleToString.eligible(key) && SimpleToString.toSimpleString(key).value),
                    keyStyle: key.type === 'number' ? {color: 'red','font-family': '"Lucida Console", Monaco, monospace'} : (SimpleToString.eligible(key) && SimpleToString.toSimpleString(key).style),
                    valueString: key.type === 'number' ? this.toLen(value, longestValue) + '(' + value.data.subtype + ')' : (SimpleToString.eligible(value) && SimpleToString.toSimpleString(value).value),
                    valueStyle: value.type === 'number' ? {color: 'red','font-family': '"Lucida Console", Monaco, monospace'} : (SimpleToString.eligible(value) && SimpleToString.toSimpleString(value).style),
                    index,
                })),
                tableOptions: {
                    headings: {
                        keyValue: 'Key',
                        valueValue: 'Value'
                    }
                }
            })
        },
        watch: {
            value() {
                this.computeValues();
            }
        },
        methods: {
            dictDepthExceeded() {
                return 1 < this.path.filter(p => typeof p[0] === "number" && ['key', 'value'].includes(p[1])).length
            },
            computeValues() {
                const longest = this.longestLengths('key');
                const longestValue = this.longestLengths('value');
                this.entries = this.value.map(({key, value}, index) => ({
                    keyValue: key,
                    valueValue: value,
                    keyString: key.type === 'number' ? this.toLen(key, longest) + '(' + key.data.subtype + ')' : (SimpleToString.eligible(key) && SimpleToString.toSimpleString(key).value),
                    keyStyle: key.type === 'number' ? {color: 'red','font-family': '"Lucida Console", Monaco, monospace'} : (SimpleToString.eligible(key) && SimpleToString.toSimpleString(key).style),
                    valueString: key.type === 'number' ? this.toLen(value, longestValue) + '(' + value.data.subtype + ')' : (SimpleToString.eligible(value) && SimpleToString.toSimpleString(value).value),
                    valueStyle: value.type === 'number' ? {color: 'red','font-family': '"Lucida Console", Monaco, monospace'} : (SimpleToString.eligible(value) && SimpleToString.toSimpleString(value).style),
                    index,
                }));
            },
            toLen(numberString, longest) {
                const [prep, postp] = numberString.split('.');
                return new Array(longest.pre).fill(' ').join('')
                + prep + (postp ? '.' + new Array(longest.post).fill(' ').join('') : '')
            },
            longestLengths(keyOrValue) {
                return this.value.filter(tup => tup[keyOrValue].type === 'number')
                    .map(({[keyOrValue]: {data: {value}}}) => value.includes('.')
                        ? {pre: value.indexOf('.') - 1, post: value.length - value.indexOf('.') - 1}
                        : {pre: value.length, post: 0}) // pre decimal point
                    .reduce((a,b) => ({pre: Math.max(a.pre, b.pre), post: Math.max(a.post, b.post)}), {pre: 0, post: 0});
            },
            determineKeyTypes(value) {
                const ret = [...new Set(value.map(val => val.key.type))];
                return ret.length > 3 ? ['mixed'] : ret;
            },
            determineEntryTypes(value) {
                const ret = [...new Set(value.map(val => val.value.type))];
                return ret.length > 3 ? ['mixed'] : ret;
            },
            display(pPart) {
                this.$emit('select', [...this.path, pPart])
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
    }

    .table {
        width: available;
        background: lightgrey;
    }

    .link {
        text-decoration: none;
        color: blue;
        cursor: pointer
    }
</style>
