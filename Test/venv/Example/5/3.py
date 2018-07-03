#5.4 条件和条件语句

#5.4.1 这就是布尔变量的作用

#真值(也叫做布尔值)

#下面的值在作为布尔表达式的时候，会被解释器看作假(false):

#False None 0 "" () [] {}

#换句话说，也就是标准值False和None，所有类型的数字0(包括浮点型，长整型和其他类型),
# 空序列（比如空字符串，元组和列表)以及空的字典都为假,其他一切都被解释为真，包括特殊值True

#也就是说,在Python中的所有值都能被解释为真值,事实上,True和False等同于1和0

print(True)
print(False)
print(True == 1)
print(False == 0)
print(True + False + 42)

#布尔值True和False属于布尔类型，bool函数可以用来(和list，str以及tuple一样）转换其他值

boolTest = bool('I think,therefore I am')
print(boolTest)
boolTest = bool(42)
print(boolTest)
boolTest = bool('')
print(boolTest)
boolTest = bool(0)
print(boolTest)

#因为所有值都可以用作布尔值，所以几乎不需要对它们进行显式转换(可以说Python会自动转换这些值)

#条件执行和if语句

#真值可以联合使用
'''
name = input('What is your name?')

if name.endswith('Gumby'):
    print('Hello,Mr.Gumby')
 '''
#这就是if语句，它可以实现条件执行.即如果条件(在if和冒号之间的表达式)判定为真，
#那么后面的语句块就会被执行，条件为假，语句块就不会被执行

#5.4.3 else子句
#else 子句不是独立的语句，而只能作为if语句的一部分
'''
name = input('What is your name?')
if name.endswith('Gumby'):
    print('Hello,Mr.Gumby')
else:
    print('Hello,stranger')
'''
#5.4.4 elif语句

#如果需要检查多个条件，就可以使用elif ,它是else if 的简写，也是if和else子句的联合使用，
#也就是具有条件的else子句
'''
num=input('Enter a number:')
num=int(num)
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The nmber is Zero')
'''
#5.4.5 嵌套代码块

#if语句里面可以嵌套使用if语句
'''
name=input('What is your name?')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello,Mr.Gumby')
    elif name.startswith('Mrs.'):
        print('Hello,Mrs.Gumby')
    else:
        print('Hello,Gumby')
else:
    print('Hello,stranger')
'''
#5.4.6 更复杂的语句

#1.比较运算符

#x == y x等于y
#...
#x != y x不等于y
#x is y x和y是同一个对象
#x is not y x和y是不同的对象
#x in y x是y容器（例如，序列）的成员
#x not in y x不是y容器（例如，序列）的成员

#在Python中比较运算和赋值运算一样是可以连接的--几个运算符可以连在一起使用，比如：
age = 50
print(0<age<100)
age = -1
print(0<age<100)

#2.相等运算符使用两个等号==，一个等号是赋值

#3. is：同一性运算符

#is 运算符是判定同一性而不是相等性的，变量x和y都被绑定到同一个列表上，
# 而变量z被绑定在另一个具有相同数值和顺序的列表上，它们的值可能相等，但是却不是同一个对象
#例1
x = y = [1,2,3]

z = [1,2,3]
print(x == y)
print(x == z)
print(x is y)
print( x is z)

#例2

x = [1,2,3]
y = [2,4]
print(x is not y)
del x[2]
y[1] = 1
y.reverse()
print(x == y)
print(x is y)

#4. in: 成员资格运算符

#成员资格运算符可以像其他比较运算符一样在条件语句中使用
'''
name=input('What is your name？')
if 's' in name:
    print('Your name contains the letter "s".')
else:
    print('Your name does not contain the letter "s".')
'''
#5. 字符串和序列比较

#字符串可以按照字母顺序排列比较
#实际的顺序可能会因为使用不同的本地化设置(locale)而和上边的例子有所不同
print('alpha' < 'beta')

ordTest = 'FnOrD'.lower() == 'Fnord'.lower()

#其他的序列也可以用同样的方式进行比较，不过比较的不是字符而是其他类型的元素

ordTest = [1,2] < [2,1]
print(ordTest)
#如果一个序列中包括其他序列元素，比较规则也同样适用于序列元素

ordTest = [2,[1,4]] < [2,[1,5]]
print(ordTest)

#布尔运算符

# 布尔运算符对语句的优化例子
'''
number = input('Enter a number between 1 and 10:')
number = int(number)
if number <= 10:
    if number >= 1:
        print('Great!')
    else:
        print('Wrong!')
else:
    print('Wrong!')
'''
#使用了and 布尔运算符之后
'''
number = input('Enter a number between 1 and 10:')
number = int(number)
if number <= 10 and number >= 1:
    print('Great!')
else:
    print('Wrong!')
'''

'''
number = input('Enter a number between 1 and 10:')
number = int(number)
if 1<=number<= 10 :
    print('Great!')
else:
    print('Wrong!')
'''

#and运算符就是所谓的布尔运算符，它连接两个布尔值，并且都在两者都为真时返回真，否则返回假，
#与它同类的还有两个运算符，or和not,使用这三个运算符就可以随意结合真值

#if ((cash > price) or customer_has_good_credit) and not out_of_stock: give_goods()

#5.4.7 断言

#if not condition:
#    crash program

age = 10
assert 0 < age < 100
age = -1
assert 0 < age < 100

age = -1
assert 0 < age < 100,'The age must be realistic'
