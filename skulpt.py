class Module:
    def __init__(self):
        self.maincode='''
var $builtinmodule = function (name) {
	var mod = {__name__: new Sk.builtin.str("mod")}
  // 使用Sk.builtin.func能让python理解这是个函数
	mod.add = new Sk.builtin.func(function(a, b) {
        return Sk.ffi.remapToJs(a) + Sk.ffi.remapToJs(b);
    });
	return mod;
}
        '''

 
