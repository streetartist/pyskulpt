from metapensiero.pj.__main__ import transform_string
import inspect
import sys
import subprocess
import re
import os.path
import ast
import astunparse

workdir = os.path.dirname(sys.argv[0])

with open(sys.argv[0]) as f:
    f.read()


'''
def get_source(func):  
    code=""
    first = True
    for line in inspect.getsourcelines(func)[0][2:]:
        if first:
            code+=line[4:]
            first=False
        else:
            code+=line
    return code

def del_waste(self, wastes):
    waste = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'build', 'generate',]
    
    production = []

    for i in wastes:
        j = getattr(self, i)

        if i not in waste and hasattr(j, "litchi") == True:
            production.insert(0, j)

    return production
'''
class Module:
    def __init__(self, name):
        self.name = name
        

    def generate(self):
        self.maincode='''
var $builtinmodule = function (name) {{
    var mod = {{__name__: new Sk.builtin.str("{name}")}}
    {func}
    return mod;
}}
        '''.format(name=self.name,func=transform_string(get_source(self.build)))

        return self.maincode


class ReWriteName(ast.NodeTransformer):
    def generic_visit(self, node):
        has_lineno = getattr(node, "lineno", "None")
        col_offset = getattr(node, "col_offset", "None")
        print(type(node).__name__, has_lineno, col_offset)
        ast.NodeTransformer.generic_visit(self, node)
        return node

    def visit_Name(self, node):
        new_node = node
        if node.id == "a":
            new_node = ast.Name(id = "a_rep", ctx = node.ctx)
        return new_node

    def visit_Import(self, node):
        if node.names == [ast.alias(nam='pyskulpt', asname=None)]:
            return None
        return node

def get_code_by_transcrypt():
    with open(workdir + "\\temp.py","w") as f:
        with open(sys.argv[0]) as source:
            f.write(re.sub("import pyskulpt","", source.read()))

    return subprocess.run(['python','-m','transcrypt', '-n',workdir + "\\temp.py"])

def get_code_by_javascripthon():
    with open(sys.argv[0]) as source:
        visitor = ReWriteName()
        root = ast.parse(source.read())
        print(astunparse.dump(root))
        root = visitor.visit(root)
        ast.fix_missing_locations(root)
        new_code = astunparse.unparse(root)
        print(new_code)
        return transform_string(new_code)# (re.sub("import pyskulpt","", source.read()))


def get_source():
    with open(sys.argv[0]) as source:
        tree =  ast.parse(source.read())
        print(astunparse.dump(tree))

print(get_code_by_javascripthon())
print(get_source())
