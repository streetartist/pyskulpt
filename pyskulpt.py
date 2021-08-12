from metapensiero.pj.__main__ import transform_string
from parse import parse
import inspect
from parser import Parser
from lexer import Lexer

lexer = Lexer()
parser = Parser()

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
        
        #parse("({}),",self.maincode)
        tokens = lexer.tokenize(self.maincode)
        tree = parser.parse(tokens)
        print(tree)
        return self.maincode
