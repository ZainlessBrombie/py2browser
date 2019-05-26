import StringDisplay from "./StringDisplay";
import PlainDisplay from "./PlainDisplay";
import Empty from "./Empty";
import ArrayDisplay from "./ArrayDisplay";
import UnknownDisplay from "./UnknownDisplay";
import DatetimeDisplay from "./DatetimeDisplay";
import FunctionDisplay from "./FunctionDisplay";
import BytesDisplay from "./BytesDisplay";
import MapDisplay from "./MapDisplay";
import RecursionDisplay from "./RecursionDisplay";
import StreamDisplay from "./StreamDisplay";
import ModuleDisplay from "./ModuleDisplay";
import PandasSeriesDisplay from "./PandasSeriesDisplay";

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
            props: (typeVar) => typeVar ? {value: typeVar.data.value, color: 'black', heading: 'Type'} : {value: 'MISSING'}
        },
        bytes: {
            component: BytesDisplay,
            props: (bytesVar) => bytesVar ? {value: bytesVar.data.value, len: bytesVar.data.len} : {},
        },
        map: {
            component: MapDisplay,
            props: (mapVar) => mapVar ? {value: mapVar.data.value, subtype: mapVar.data.subtype} : {}
        },
        recursion: {
            component: RecursionDisplay,
            props: (recVar) => recVar ? {depth: recVar.data.value} : {}
        },
        stream: {
            component: StreamDisplay,
            props: (streamVar) => streamVar ? {name: streamVar.data.name, mode: streamVar.data.mode, encoding: streamVar.data.encoding, closed: streamVar.data.closed} : {}
        },
        module: {
            component: ModuleDisplay,
            props: (modVar) => modVar ? {name: modVar.data.name, moduleToString: modVar.data.to_string} : {}
        },
        none: {
            component: PlainDisplay,
            props: () => ({value: 'None', color: 'purple'})
        },
        pandas_series: {
            component: PandasSeriesDisplay,
            props: (seriesVar) => seriesVar ? {length: seriesVar.data.full_length, id: seriesVar.id, head: seriesVar.data.value, dType: seriesVar.data.dtype} : {}
        }
    }
}
