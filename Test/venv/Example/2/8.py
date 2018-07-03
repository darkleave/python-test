#成员资格

permissions = 'rw'
isIn1 = 'w' in permissions
print('isIn1:' + str(isIn1))
isIn2 = 'x' in permissions
print('isIn2:' + str(isIn2))
users = ['mlh','foo','bar']
isIn3 = input('Enter your user name: ') in users
print('isIn3:' + str(isIn3))
subject = '$$$ Get rich now!!! $$$'
isIn4 = '$$$' in subject
print('isIn4:' + str(isIn4))