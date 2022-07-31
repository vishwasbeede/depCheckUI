const { boolean, string } = require("yargs");
const arguments = require("yargs");
//{'wfn': 'fgh', 'src': 'fgh', 'dst': 'fgh', 'stkn': 'fgh', 'dtkn': 'fgh', 'dry': 'off', 'comp': 'on'}
const argv = arguments.command('run','Pre Validates Workflow informations',{
    wfn:{
        description: 'Enter workflow name',
        alias:'w',
        type: 'String'
    },
    src:{
        description: 'Source target URL',
        alias:'s',
        type: 'String'
    },
    dst:{
        description: 'Destination target URL',
        alias:'d',
        type: 'String'
    },
    stkn:{
        description: 'Target token info',
        alias:'S',
        type: 'String'
    },
    dtkn:{
        description: 'Destination token info',
        alias:'D',
        type: 'string'
        }
}).help().alias('help','h').argv;
// console.log(argv._)
console.log(JSON.stringify(argv))

