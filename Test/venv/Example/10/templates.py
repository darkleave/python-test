import fileinput,re

#匹配括号里的字段:
field_pat = re.compile(r'\[(.+?)\]')

#收集变量
scope = {}

#用于re.sub中:

def replacement(match):
    code = match.group(1)
    try:
        #如果字段可以求值,返回它:
        return str(eval(code,scope))
    except SyntaxError:
        #否则执行相同作用域内的赋值语句……
        exec(code,scope)
        #返回空字符串:
        return ''
#将所有文本以一个字符串的形式获取:
lines = []
for line in fileinput.input('a.txt',openhook=fileinput.hook_encoded('UTF-8')):
    lines.append(line)
text = ''.join(lines)
print(text)
#将field模式的所有匹配项都替换掉:
print(field_pat.sub(replacement,text))
#此处将replacement函数作为参数,text的每个匹配项会依次作为参数传入replacement函数，并将replacement函数
#的返回值替换到text当中
#第一次[x = 2], 执行exec(code,scope) 返回''
#第二次[y = 3], 执行exec(code,scope) 返回''
#第三次[x], 返回 2
#第四次[y], 返回 3
#第五次[x+y],返回 5
'''
最终结果:
''
''
The sum of 2 and 3 is 5.
'''

