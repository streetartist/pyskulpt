# pyskulpt
Use python to develop Skulpt

使用Python开发Skulpt扩展库

## Demo
```python
from pyskulpt import Module

class mod(Module):
    def __init__(self):
        self.name= "mod"
    def build():
        # 使用Sk.builtin.func能让python理解这是个函数
        mod.add = Sk.builtin.func(lambda a, b: Sk.ffi.remapToJs(a) + Sk.ffi.remapToJs(b))
m = mod().generate()
print(m)
```
输出
```javascript
var $builtinmodule = function (name) {
    var mod = {__name__: new Sk.builtin.str("mod")}
    mod.add = Sk.builtin.func((a, b) => {
    return (Sk.ffi.remapToJs(a) + Sk.ffi.remapToJs(b));
});

    return mod;
}
```

## 用法
