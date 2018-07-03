#4.2.3 字典的格式化字符串
phonebook = {'Beth':'9102','Alice':'2341','Cecil':'3258'}
print("Cecil's phone number is %(Cecil)s." % phonebook)

#除了增加的字符串键以外，转换说明符还是像以前一样工作，当以这种方式使用字典的时候，
#只要所有给出的键都能在字典中找到，就可以使用任意数量的转换说明符
#这类字符串格式化在模板系统中非常有用
template = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''
data = {'title':'My Home Page','text':'Welcome to my home page!'}
print(data)
print(template % data)
