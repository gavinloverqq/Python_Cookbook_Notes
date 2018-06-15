## __iter__,iter,__next__,next,generator之间的关系

在使用Python的过程中，我们经常进行for循环输出，特别是对容器进行循环处理使用起来特别的方便。
比如：
```
# 对字符串迭代
for s in “helloworld”:
  print(s)

# 对字典迭代
for key in {“a": 1, “b”: 2}:
  print(key)
```
那它是怎么做到的呢， 我们如何实现一个这样的for循环对象呢？
在进行for循环时，首先会调用iter这个内建函数,这个函数需要返回一个可迭代的对象(定义了__next__这个魔法方法的对象，在Python2.7中是next这个方法的对象)，然后每次循环输出时, 调用next这个内建函数。在输出结束时，__next__魔法函数应该引发StopIteration异常，for循环捕捉此异常循环输出结束。
举个例子:
```
class IterDemo(object):

  def __init__(self):
    self.count = 0

  def __iter__(self):
    # 该函数会由iter函数调用 返回一个可以迭代的对象 
    return self

  def __next__(self):
    # 该函数会由next内建函数调用
    if self.count < 10:
      self.count += 1
      return "__next__ : %s" % self.count
    else:
      raise StopIteration


if __name__ == "__main__":
  it = IterDemo()

  for i in it:
    print(i)
```
上面这个代码就实现了一个可迭代的对象，可以进行一个for循环输出。注意上面的代码在Python2.7中执行会出错。这是因为Python2.7中的next内建函数是调用对象的next方法而不是__next__方法。
下面代码可以在python3.5中和Python2.7中均可执行。
```
class IterDemo(object):

  def __init__(self):
    self.count = 0

  def __iter__(self):
    # 该函数会由iter函数调用 返回一个可以迭代的对象 
    return self

  def __next__(self):
    # 该函数会由next内建函数调用
    if self.count < 10:
      self.count += 1
      return "__next__ : %s" % self.count
    else:
      raise StopIteration

  def next(self):
    # 该函数会由next内建函数调用
    if self.count < 10:
      self.count += 1
      return "next : %s" % self.count
    else:
      raise StopIteration

if __name__ == "__main__":
  it = IterDemo()
  for i in it:
    print(i)
    
```
总的来说iter和next是Python内建函数，一个调用示例的__iter__方法返回可迭代对象，一个调用__next__(python2中是next)方法进行每次迭代。
关于生成器generator
当一个函数中有yield关键字，就是一个生成器对象，一个生成器对象不会立即执行。只有执行next(g)或者g.send()的时候，才会去执行。每次进行一个next，会执行一个yield，然后到下一次的yield暂停。当所有的yield结束后，会自动引发一个StopIteration。
注: next(g)和g.send(None)相同 对于需要接收输入值的生成器可能不能使用next()
生成器实现了迭代器的所有操作，也就是只要它是一个生成器肯定是可以进行迭代的。生成器除了具有迭代功能，而且特别高效，yield生成器是实现协程的基础。
一个示例:
``` 
def generator_noinput():
    yield "out: 1"
    yield "out: 2"
    yield "out: 3"

def genrator_input():
    i = yield "out: 1"
    # 上面这句话可以理解为类似这样的伪代码 可能不是很准确 但更容易理解

    # output( "out: 1")
    # i = input()

    i = yield "last in : %s" % i
    print(i)


if __name__ == "__main__":


    for g in generator_noinput():
      print g

    ig = genrator_input()

    # 第一次进行迭代时 发送的值必须为None
    print(ig.send(None))
    print ig.send("input")
    try:
        ig.send("input2")
    except StopIteration:

        pass
        
```