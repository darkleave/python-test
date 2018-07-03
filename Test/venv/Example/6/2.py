#6.4.3 关键字参数和默认值

#不带参数名的参数我们称为位置参数
#在参数很多，参数顺序难以记住的时候，可以使用关键字参数
#使用参数名提供的参数叫做关键字参数，，它的主要作用在于可以明确每个参数的作用
def hello_l(greeting,name):
    print('%s ,%s!' % (greeting,name))
hello_l(greeting='Hello',name='world')
hello_l(name='world',greeting='Hello')

#使用关键字函数 可以给参数提供默认值

def hello_3(greeting='Hello',name='world!'):
    print('%s,%s !' % (greeting,name))

hello_3()
hello_3('Greetings')#位置参数
hello_3('Grettings','universe')

#位置参数和关键字参数联合使用，位置参数放在前面
def hello_4(name,greeting='Hello',punctuation='!'):
    print('%s,%s%s' % (greeting,name,punctuation))

hello_4('Mars')
hello_4('Mars','Howdy')
hello_4('Mars','Howdy','...')
hello_4('Mars',punctuation='.')
hello_4('Mars',greeting='Top of the morning to ya')


#6.4.4 收集参数

def print_params(*params):
    print(params)

print_params('Testing')

print_params(1,2,3)

#参数前的星号将所有值放置在同一个元组中.
def print_params_2(title,*params):
    print(title)
    print(params)

print_params_2('Params:',1,2,3,)

#由上可见星号的意思就是"收集其余的位置参数",如果不提供任何供收集的元素，params就是个空元祖:

print_params_2('Nothing:')

#无法处理关键字参数，抛出异常

#print_params_2('Hmm...',something=42)

#双星号处理关键字

def print_params_3(**params):
    print(params)

print_params_3(x=1,y=2,z=3)

#结果返回字典

def print_params_4(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(*pospar)
    print(keypar)

print_params_4(1,2,4,5,6,7,foo=1,bar=2)

print_params_4(1,2)

#初始化函数
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

#获得名字的函数: 通过get避免抛出异常，查询不到的情况下返回None,data[label][name]会抛出异常
def lookup(data,label,name):
    return data[label].get(name)


def store(data,*full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1,'')
        labels = 'first','middle','last'
        print(zip(labels,names))
        for label,name in zip(labels,names):
            people = lookup(data,label,name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

d = {}
init(d)
store(d,'Han solo')

store(d,'Luke Skywalker','Anakin Skywalker')
result = lookup(d,'last','Skywalker')

print(result)


#6.4.5 参数收集的逆过程

def add(x,y): return x + y

params = (1,2)

addResult = add(*params)
print(addResult)

#列表也可以
paramTest = [1,2]
addResult = add(*paramTest)

print(addResult)

#使用双星号处理字典

params = {'name':'Sir Robin','greeting':'Well met'}
hello_3(**params)

#在定义或者调用函数时使用星号(或者双星号)仅传递元组和字典

def with_stars(**kwds):
    print(kwds['name'],'is',kwds['age'],'years old')

def without_stars(kwds):
    print(kwds['name'],'is',kwds['age'],'years old')
args = {'name':'Mr.Gumby','age':42}
with_stars(**args)

without_stars(args)

#在with_stars中，我在定义和使用函数时都使用了星号.而在without_stars中两处都没用，但得到了同样的结果。
#所以星号只在定义函数（允许使用不定数目的参数)或者调用（分割字典或者序列）时才有效.

def foo(x,y,z,m=0,n=0):
    print(x,y,z,m,n)

def call_foo(*args,**kwds):
    print('Calling foo!')
    foo(*args,**kwds)

call_foo(1,2,3,m=1,n=2)

#6.4.6 练习使用参数

def story(**kwds):
    return 'Once upon a time,there was a ' \
           '%(job)s called %(name)s.' % kwds

def power(x,y,*others):
    if others:
        print('Received redundant parameters:',others)
    return pow(x,y)

def interval(start,stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:  #如果没有为stop提供值
        start,stop = 0,start #指定参数
    result = []
    i = start  #计算start索引
    while i < stop: #直到计算到stop的索引
        result.append(i) #将索引添加到result内
        i+=step #用step(>0)增加索引i
    return result

print(story(job='king',name='Gumby'))

print(story(name = 'Sir Robin',job='brave knight'))

params = {'job':'lanaguage','name':'Python'}
print(story(**params))

del params['job']
print(story(job='stroke of genius',**params))

result = power(2,3)
print(result)
result = power(3,2)
print(result)
result = power(y=3,x=2)
print(result)

params = (5,) * 2
print(params)
result = power(*params)
print(result)

result = power(3,3,'Hello,world')
print(result)

interval(10)

interval(1,5)

interval(3,12,4)
result = power(*interval(3,7))

print(result)

#6.5作用域
#什么是变量，你可以把它们看成是值的名字,变量和所对应的值是可"不可见"的字典.内建的vars函数可以返回这个字典

x = 1
scope = vars()
resultX = scope['x']
print(resultX)
scope['x'] += 1
print(x)

#这类不可见字典叫做命名空间或者作用域.除了全局作用域外,每个函数调用都会创建一个新的作用域:

def foo(): x = 42
x = 1
foo()
print(x)

#foo 函数重新改变了变量x,但最终x的值并没有改变,这是因为当调用foo的时候，新的命名空间就被创建了,它作用于foo内的代码块.
#赋值语句x=42只在内部作用域(局部命名空间)起作用,所以它并不影响外部(全局)作用域中的x.
#函数内的变量被称作局部变量

#globals函数获取全局变量值,该函数的近亲是vars,它可以返回全局变量的字典(locals返回局部变量的字典)

#重新绑定全局变量

x = 1
def change_global():
    global x
    x = x + 1
change_global()
print(x)

#嵌套作用域

def foo():
    def bar():
        print('Hello,world')
    bar()

#嵌套的突出作用,例如需要用一个函数”创建“另一个：
def multiplier(factory):
    def multiplyByFactory(number):
        return number*factory
    return multiplyByFactory

#一个函数位于另外一个里面,外层函数返回里层函数,也就是说函数本身被返回了,但并没有被调用,
#重要的是返回的函数还可以访问它的定义所在的作用域,换句话说,它”带着“它的环境(和相关的局部变量)

#每次调用外层函数，它内部的函数都被重新绑定，factory变量每次都有一个新的值.由于Python的嵌套作用域
#来自(multiplier的)外部作用域的这个变量，稍后会被内层函数访问,例如：


double = multiplier(2)
result = double(5)
print(result)
#可以看到2这个变量值仍被double所持有
triple = multiplier(3)
result = triple(3)
print(result)

result = multiplier(5)(4)
print(result)

#类似multiplyByFactory函数存储子封闭作用域的行为叫做闭包(closure)

#外部作用域的变量一般来说是不能进行重新绑定的,但在；Python 3.0中，nonlocal关键字被引入.
#它和global关键字的使用方式类似,可以让用户对外部作用域(但并非全局作用域)的变量进行赋值.





