from ast import arguments
from typing import Dict
import flask
import subprocess
import json
app = flask.Flask(__name__)
render_templates = flask.render_template
request = flask.request

@app.route('/')
def hello():
    return render_templates('index.html')

def dry_run_val(op):
    # print('Workflow name',op['wfn'])
    # print('Workflow source URL',op['src'])
    # print('Workflow target URL',op['dst'])
    # print('Workflow source token',op['stkn'])
    # print('Workflow target token',op['dtkn'])
    # print("Vishwas Beede")
    p = subprocess.Popen(['node',r'test.js'],stdout=subprocess.PIPE)
    out = p.stdout.read()
    print(out)
    return ("<h6>This will performs PreValidations of inputs</h6><h4>%s</h4><a href='/'>Home</a>"%(out))
    # return 'Dry run intial input validation'

def actual_run_val(op):
    # wsdSD
    try:
        print('Workflow name',op['wfn'])
        print('Workflow source URL',op['src'])
        print('Workflow target URL',op['dst'])
        print('Workflow source token',op['stkn'])
        print('Workflow target token',op['dtkn'])
    except KeyError:
        return ("Please enter all parameters details")

    argumentslists = ['node',"preValidate.js",
    'run','-w',op['wfn'],'-s',op['src'],'-d',op['dst'],'-S',op['stkn'],'-D',op['dtkn']]
    if 'comp' in dict.keys(op) :
        argumentslists.extend(['-A','all'])
        print(argumentslists)
        #This Need to validate all components
    else:
        append_operations_data=''
        choose = ['ada','aap','tra','wfs','pbks']
        for k in choose:
            if(k in dict.keys(op)):
                append_operations_data+=k+','
        # print('----------------')
        argumentslists.extend(['-A',append_operations_data])
        # print(append_operations_data)
        
    p = subprocess.Popen(argumentslists ,stdout=subprocess.PIPE)
    out = p.stdout.read().decode('utf-8')
    outformatted = json.loads(out)
    print(outformatted.keys())
    return ("<h6>This will performs PreValidations of inputs</h6><h4>%s\
        </h4><a href='/'>Home</a>"%(outformatted))
    

@app.route('/v1/api/depCheck')
def depCheck():
    options = request.args.to_dict()
    print(type(options))
    print(options)
    dry_run=options.get('dry')
    if dry_run == 'on':
        print('Dry run is %s'%dry_run)
        return dry_run_val(options)
    else:
        print('Dry run is %s', dry_run)
        print('Running actual dependency check')
        # return 'Check all dependencies'
    return actual_run_val(options)

if __name__ == '__main__':
    app.run('0.0.0.0',8092,debug=True)