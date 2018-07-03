#10.3.7
#shelve
#shelve 是一个简单的存储方案,shelve 中唯一有趣的函数是open,在调用它的时候(实用文件名为参数),
#它会返回一个Shelf对象,你可以把它当作普通的字段（键一定要作为字符串)来存储内容,在完成工作之后，调用close方法。
#note: shelve.open 函数返回的对象并不是普通的映射.
import shelve
s = shelve.open('test.data')
s['x'] = ['a','b','c']
s['x'].append('d')
print(s['x'])

#d没有被正确存储，原因是s['x'].append('d')得到的只是一个副本

#正确的存储方式

temp = s['x']
temp.append('d')
s['x'] = temp
print(s['x'])

#2. 简单的数据库示例

import sys,shelve

def store_person(db):
    '''
    Query user for data and store it in the shelf object
    :param db:
    :return:
    '''
    pid = input('Enter unique ID number:')
    person = {}
    person['name'] = input('Enter name: ')
    person['age'] = input('Enter age:')
    person['phone'] = input('Enter phone number:')

    db[pid] = person

def lookup_person(db):
    '''
    Query user for ID and desired field, and fetch the corresponding data from
    the shelf object
    :param db:
    :return:
    '''
    pid = input('Enter ID number: ')
    field = input('What would you like to know?(name,age,phone)')
    field = field.strip().lower()
    print(field.capitalize() + ':',db[pid][field])

def print_help():
    print('The available commands are:')
    print('store : Stores information about a person')
    print('lookup: Looks up a person from ID number')
    print('quit:Save Changes and exit')
    print('? : Prints this message')

def enter_command():
    cmd = input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open(r'./database.dat') # You may want to change this name
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()

if __name__ == '__main__': main()
