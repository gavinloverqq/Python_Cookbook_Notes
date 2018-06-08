import threading


# 线程局部存储（tls），对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。
local = threading.local()
local.tname = "main"

def func(info):
    local.tname = info
    print (local.tname)

t1 = threading.Thread(target=func, args=['funcA'])
t2 = threading.Thread(target=func, args=['funcB'])

t1.start()
t1.join()

t2.start()
t2.join()

print (local.tname)