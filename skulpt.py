class Module:
    def __init__(self, name):
        self.maincode='''
var $builtinmodule = function (name) {{
	var mod = {{__name__: new Sk.builtin.str("{name}")}}

	return mod;
}
        '''.format(name=name)

 
