<template>
    <div>
        <div class="search-bar">
            <!--suppress HtmlFormInputWithoutLabel -->
            <input placeholder="Search..." v-model="searchString" v-on:input="() => setSearch(searchString) || execSearch()">
        </div>
        <table class="w100" style="border-collapse: collapse">
            <thead class="w100 t-head">
            <tr>
                <th v-for="(col, index) in columns" class="t-field" :style="{'background-color': (index % 2) ? darkBg : lightBg}">
                    {{col && (headings || {})[col] || col}}
                </th>
            </tr>
            </thead>
            <tbody class="w100">
            <tr v-for="(row, rowIndex) in currentRows" class="t-row">
                <td v-for="(col, colIndex) in columns"
                    :style="obtainEntryStyle(rowIndex, colIndex)"
                    class="t-field">
                    <slot v-if="$scopedSlots[col]" :name="col" v-bind="{column: col, row: row, index: rowIndex}"></slot>
                    <i v-else style="font-style: normal; color: black;">{{row[col]}}</i>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: "CustomTable",
        props: {
            columns: {
                type: Array,
                default: () => []
            },
            rows: {
                type: Array,
                default: () => []
            },
            headings: {
                type: Object,
                default: () => ({})
            },
            sortCompareFunctions: {
                type: Object,
                default: () => ({})
            },
            rowWeights: {
                type: Object,
                default: () => ({})
            },
            lightBg: {
                type: String,
                default: '#f0f0f0'
            },
            darkBg: {
                type: String,
                default: '#d3d3d3'
            },
            forceEqualLength: {
                type: Boolean,
                default: false,
            }
        },
        data() {
            return {
                currentRows: [...this.rows],
                sortingColumn: undefined,
                desiredSearch: '',
                isSearching: false,
                searchString: '',
                rowsDirty: false,
            };
        },
        watch: {
            rows() {
                this.rowsDirty = true;
                this.execSearch();
            }
        },
        methods: {
            obtainEntryStyle(rowIndex, colIndex) {
                return {
                    'flex-grow': 1,
                    'background-color': !!(rowIndex % 2) ^ !!(colIndex % 2) ? this.lightBg : this.darkBg,
                    ...(this.forceEqualLength ? {'width': `${100 / this.columns.length}%`} : {})
                };
            },
            setSearch(str) {
                this.desiredSearch = str;
            },
            execSearch() {
                const before = this.desiredSearch;
                if (this.isSearching) return;
                this.isSearching = true;
                this.rowsDirty = false;
                try {
                    this.currentRows = this.rows
                        .filter(entry => entry)
                        .filter(entry => Object.values(entry)
                            .map(f => `${f}`.toLowerCase().includes(before.toLowerCase()))
                            .reduce((a, b) => a || b, false));
                } finally {
                    this.isSearching = false;
                    if (this.desiredSearch !== before || this.rowsDirty) this.execSearch(this.desiredSearch);
                }
            }
        }
    }
</script>

<style scoped>
    .search-bar {
        padding: 7px;
        background-color: #b0b0b0;
        border-bottom: 1px solid black;
    }

    .t-row {
        background: mediumaquamarine;
        width: 100%;
    }

    .t-field {
        padding: 7px;
        overflow: hidden;
    }

    .t-head {
        border-bottom: 1px solid black;
    }

    .w100 {
        width: 100%;
    }
</style>
