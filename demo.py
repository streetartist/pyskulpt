from pyskulpt import Module

class mod(Module):
    def build():
        # 使用Sk.builtin.func能让python理解这是个函数
	mod.add = Sk.builtin.func(lambda a, b: return Sk.ffi.remapToJs(a) + Sk.ffi.remapToJs(b))
