

const eligible = (v) => {
    return ['string', 'number', 'datetime', 'boolean'].includes(v.type);
};

const toSimpleString = (v) => {
    if (v.type === 'string') {
        return {
            value: JSON.stringify(v.data.value),
            style: {
                color: 'green',
                'font-family': '"Lucida Console", Monaco, monospace'
            }
        };
    }
    if (v.type === 'number') {
        return {
            value: `${v.data.value} (${v.data.subtype})`,
            style: {
                color: 'red',
                'font-family': '"Lucida Console", Monaco, monospace'
            }
        }
    }
    if (v.type === 'datetime') {
        return {
            value: `${v.data.value} (${v.data.subtype})`,
            style: {
                color: 'blue',
                'font-family': '"Lucida Console", Monaco, monospace'
            }
        }
    }
    if (v.type === 'boolean')  {
        return {
            value: v.data.value ? 'True' : 'False',
            style: {
                color: 'orange',
                'font-family': '"Lucida Console", Monaco, monospace'
            }
        }
    }
    return {
        value: 'ERROR: UNKNOWN TYPE ' + v.type,
        style: {
            color: 'red',
        }
    }
};

export default {
    eligible,
    toSimpleString,
};
