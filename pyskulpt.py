import sys
import subprocess
import re
import os.path
from redbaron import RedBaron, DefNode, DefArgumentNode

workdir = os.path.dirname(sys.argv[0])
filename = os.path.filename(sys.argv[0])[:-3]

def get_function(code):
    red = RedBaron(code)
    
    deflist = {}
    for i in red:
        if isinstance(i,DefNode):
            arg = []
            for j in i.arguments:
                if isinstance(j,DefArgumentNode):
                    arg.append(j.target.value)
              
            deflist[i.name]=arg[:]
    
    return deflist

def get_code_by_transcrypt():
    with open(workdir + "\\temp.py","w") as f:
        with open(sys.argv[0]) as source:
            f.write(re.sub("import pyskulpt","", source.read()))

    return subprocess.run(['python','-m','transcrypt', '-n',workdir + "\\temp.py"])

def generate_library():
    with open(workdir + "\\temp.py","w") as f:
        source = f.read()
        deflist = get_function(source)
        
        func = ""
        for i in deflist.items():
            args = ""
            params = ""
            for j in i[1]:
                args += j+","
                params += j+"="+j+","

            func += '''
mod.{name} = new Sk.builtin.func(function({args}) {{
        return Sk.ffi.remapToJs({name}({params}));
    }});
            '''.format(args=args,name=i[0],params=params)
            
        library = '''
var $builtinmodule = function (name) {{
    var mod = {{__name__: new Sk.builtin.str({name}")}}
    {func}
    return mod;
}}
        '''.format(name=filename,func=func)
        
    with open(workdir + "\\sk_"+ filename, "w") as f:
        f.write(library)
