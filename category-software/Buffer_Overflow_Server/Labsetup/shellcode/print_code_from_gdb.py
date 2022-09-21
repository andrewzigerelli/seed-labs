
gdb.execute('start')
print('STARTED')
stringss = gdb.execute('si', False, True)
print(stringss)
print(len(stringss))
with open('test_out.txt', 'w') as f:
    f.write(stringss)
