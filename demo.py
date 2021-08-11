from pyskulpt import Module

class mod(Module):
    def __init__(self):
        self.name= "mod"
    def build():
        # 使用Sk.builtin.func能让python理解这是个函数
        mod.add = Sk.builtin.func(lambda a, b: Sk.ffi.remapToJs(a) + Sk.ffi.remapToJs(b))
m = mod().generate()
print(m)
