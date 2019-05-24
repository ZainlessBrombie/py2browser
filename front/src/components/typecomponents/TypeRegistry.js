import StringDisplay from "./StringDisplay";
import PlainDisplay from "./PlainDisplay";
import Empty from "./Empty";
import ArrayDisplay from "./ArrayDisplay";
import UnknownDisplay from "./UnknownDisplay";
import DatetimeDisplay from "./DatetimeDisplay";
import FunctionDisplay from "./FunctionDisplay";
import BytesDisplay from "./BytesDisplay";

export default {
    obtain(v, path) {
        if (!v) return {
            component: Empty,
            props: () => ({ path })
        };

        return this.typeMap[v.type] ? {
            component: this.typeMap[v.type].component,
            props: (val) => ({...this.typeMap[v.type].props(val), path}),
        } : { component: UnknownDisplay, props: () => ({ path, value: v }) }
    },
    typeMap: {
        string: {
            component: StringDisplay,
            props: (stringVar) => stringVar ? ({value: stringVar.data.value}) : {value: '' /* wont be rendered */}
        },
        number: {
            component: PlainDisplay,
            props: (numberVar) => numberVar ? ({value: numberVar.data.value, color: 'red'}) : {value: 'MISSING'}
        },
        collection: {
            component: ArrayDisplay,
            props: (arrayVar) => arrayVar ? { value: arrayVar.data.value, subtype: arrayVar.data.subtype } : { value: [], subtype: 'Unknown' }
        },
        datetime: {
            component: DatetimeDisplay,
            props: (dateVar) => dateVar ? { value: dateVar.data.value, subtype: dateVar.data.subtype } : { value: 'MISSING' }
        },
        boolean: {
            component: PlainDisplay,
            props: (boolVar) => boolVar ? {value: boolVar.data.value.toString(), color: 'orange'} : {value: 'MISSING'}
        },
        'function': {
            component: FunctionDisplay,
            props: (funcVar) => funcVar ? {toStr: funcVar.data.to_string, module: funcVar.data.module, filename: funcVar.data.filename, argCount: funcVar.data.arg_count} : {value: 'MISSING'}
        },
        type: {
            component: PlainDisplay,
            props: (typeVar) => typeVar ? {value: 'Module: ' + typeVar.data.value, color: 'black'} : {value: 'MISSING'}
        },
        bytes: {
            component: BytesDisplay,
            props: (bytesVar) => bytesVar ? {value: bytesVar.data.value, len: bytesVar.data.len} : {},
        }
    }
}
