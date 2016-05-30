###研究window服务什么的###



1. ps.py

   ####说明####

   - [目前代码源自](http://blog.csdn.net/ghostfromheaven/article/details/8604738)加了一点改动
   - [获得帮助的一点内容](http://zhangley.com/article/python-service-hotkey/)

   ####使用####
   - 在原有基础上改了一点现在可以记录开机时长
   - 在同级目录下做了写了个service.log。。
   - 在管理员权限下的cmd使用
     - ps.py (--startup auto) install 
     - ps.py (re)start/remove/update/stop