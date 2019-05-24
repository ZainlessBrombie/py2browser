
export default {
    deepEquals: (a, b, visited) => {
        if (visited.includes(a) && visited.includes(b)) return false; // loop.
        if (typeof a !== typeof b) return false;
        if (a === b) return true;
        if (typeof a === 'object') {
            const aKeys = new Set(Object.keys(a));
            const bKeys = new Set(Object.keys(b));
            if (aKeys.size !== bKeys.size) return false;
            if (!Object.keys(a).map(a => bKeys.has(a)).reduce((a,b) => a && b, true)) return false;

            return Object.keys(a).map(k => this.deepEquals(a[k], b[k], visited ? [...visited, a, b] : [a, b]))
                .reduce((a,b) => a && b, true);
        }
        return false; // unhandled
    },
};
