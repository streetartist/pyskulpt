class Module:
    def __init__(self, name):
        self.name = name
        self.maincode='''
var $builtinmodule = function (name) {{
	var mod = {{__name__: new Sk.builtin.str("{name}")}}
        {func}
	return mod;
}}
        '''.format(name=self.name)

    def generate():
        
        self.maincode=self.maincode.format(func=func_code)

 
