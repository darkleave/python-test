#第八章 异常

#8.1 什么是异常

#Python 用异常对象(exception object) 来表示异常情况.遇到错误后，会引发异常,如果异常对象并未被处理或捕捉，
#程序就会用所谓的回溯(traceback,一种错误信息)终止执行.

#引发一个没有任何有关错误信息的普通异常.Exception 同时也是所有异常的基类
#raise Exception

#添加了错误信息
#raise Exception('hyperdrive overload')

#在Python 3中 exceptions 模块已经被移除
#import exceptions

#所有异常都可以通过raise语句引发
#raise ArithmeticError

#继承异常基类，创建自定义异常类

class SomeCustomException(Exception): pass

#8.3 捕捉异常

#在Python 3.0中，’/’总是执行真除法，不管操作数的类型，都会返回包含任何余数的浮点结果；’//’执行Floor除法，
# 截除掉余数并且针对整数操作数返回一个整数，如果有任何一个操作数是浮点数，则返回一个浮点数

'''

try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(type(int(x)))
    xint = int(x)
    yint = int(y)
    result = xint / yint
    print(result)
    test = type(result)
    print(test)
except ZeroDivisionError:
    print("The second number can't be zero!")

'''
#传递异常
#如果捕捉到了异常,但是又想重新引发它,(也就是说要传递异常,不进行处理),
#那么可以不带参数的raise（还能在捕捉到异常时显示地提供具体异常)

#python 的方法在出现异常时，若处理异常后没有返回值，会隐式地返回None
class MuffledCalculator:
    muffled = False
    def calc(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

calculator = MuffledCalculator()

calculator.calc('10/2')

#calculator.calc('10/0')

calculator.muffled = True
result = calculator.calc('10/0')
print(result)

#8.4 不止一个except 子句
'''

try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    x = int(x)
    y = int(y)
    print(x/y)
except ZeroDivisionError:
    print('The second number cant be zero!')
except ValueError:
    print('Value Error')
except TypeError:
    print("That wasn't a number,was it?")
'''
#8.5 用一个块捕捉两个异常
#8.6 捕捉对象
'''
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    x = int(x)
    y = int(y)
    print(x/y)
except (ZeroDivisionError,ValueError,TypeError) as e:
    print('Error,Error,Error!')
    print(e)

'''
#8.7 真正的全捕捉

'''
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print(x/y)
except:
    print('Something wrong happened...')

'''
#8.8 万事大吉，try/except else 语法
#当发生异常被捕获的情况，else不会再执行
try:
    print('A simple task')
except:
    print('What? something went wrong!')
else:
    print('Ah...It went as planned')

try:
    print('A simple task')
    raise Exception
except:
    print('What? something went wrong!')
else:
    print('Ah...It went as planned')
'''
while True:
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')
        value = int(x)//int(y)
        print('x/y is',value)
    except:
        print('Invalid input,Please try again.')
    else:
        break
'''
#空的except子句会捕捉所有Exception类的异常及其所有子类的异常,
#但是百分百捕捉到所有异常是不可能的，因为try/except 语句中的代码可能会出问题,
#比如使用旧风格的字符串异常或者自定义的异常类不是Exception类的子类

#8.9 最后... finally 子句
'''
x = None
try:
    x = 1/0
finally:
    print('Cleaning up')
    del x
'''

#try except else finally
try:
    1/0
except:
    print('Unknown variable')
else:
    print('That went well!')
finally:
    print('Cleaning up.')

#异常和函数

#异常在函数内引发而不被处理，他就会传播至函数调用的地方,
#如果那里也没有处理异常，他就会继续传播,一直到达主程序(全局作用域)
#如果那里也没有处理异常,程序会带着栈跟踪终止.

#8.11 异常之禅

#异常处理try/except/else/finally 能使你忽略一些可能会产生的异常，
#这样做的原因是能够使代码更加简洁明快，而不是产生大量的if/else语句

def describePerson(person):
    print('Description of',person['name'])
    print('Age:',person['age'])
    try:
        print('Occupation:' + person['occupation'])
    except KeyError:pass

person = {'name':'小明','age':'11'}
describePerson(person)


#8.12 小结

#异常对象,异常情况(比如发生错误)可以用异常对象表示。它们可以用几种方法处理，
#但是如果忽略的话，程序就会中止

#警告
#警告类似于异常,但是(一般来说)仅仅打印错误信息.
#引发异常
#可以使用raise语句引发异常.它接受异常类或者异常实例作为参数.还能提供两个参数（异常和错误信息).
#如果在except子句中不使用参数调用raise,它就会“重新引发”该子句捕捉到的异常.

#自定义异常类
#用继承Exception类的方法可以创建自己的异常类
#捕捉异常
#使用try语句的except子句捕捉异常.如果在except子句中不特别指定异常类,那么所有的异常都会被捕捉
#异常可以放在元组中以实现多个异常的指定.如果给except提供两个参数，第二个参数就会绑定到异常对象上(except Exception as e).
#同样，在一个try/except语句中能包含多个except子句,用来分别处理不同的异常.

#else子句,除了except子句，可以使用else子句。如果主try块中没有引发异常,else子句就会被执行(try/except/else)

#finally
#如果需要确保某些代码不管是否有异常引发都要执行（比如清理代码），那么这些代码可以放置在finally子句中.
#异常和函数
#在函数内引发异常时，它就会被传播到函数调用的地方（对于方法也是一样).
