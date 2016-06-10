## 一些关于import的事。

- 一个东西第一次被import了就会生成.pyc或者其他的二进制文件（编译啥啥的）
- import 的路径应该是环境变量涉及到的，还有当前目录
- 若是要import某个目录下的，要 import xxx.xxx
- import 相当于跑了一遍这些代码吧，请注意。
  - 所以经常有`if __name__ == '__main__':`的东西
  - import时并不会执行if里的内容
- 以下是main.py 的运行结果。

```
from x.p1 import *
a,b= 1 2
-----------
import p1
p1.a,p1.b= 3 4
a,b= 1 2
-----------
from p1 import *
a,b= 3 4
```