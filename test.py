#print(int(input("age:")))
fname = "Sasha"
lname = "Gray"
print ("hello,", fname, lname)
print ("hello, %s %s" % (fname, lname))
print ('{}'.format(['e1', 'e2', 'e3']))
print("{:>20} {:>20} {:>20}".format('asd', 'qwe', 'zxc'))
print("{:.3f}".format(5.0/3))
print('Третий элемент: {2}; Второй элемент: {1}; Первый элемент: {0}'.format('el_1', 'el_2', 'el_3'))

ip = '192.168.1.4'
mask = 10
print(f"ip-params: {ip}, mask: {mask}")

octets = ['10', '1', '1', '1']
mask = 10
print(f"ip-params: {'.'.join(octets)}, mask: {mask}")

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
print(f'''IP address: {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}''')