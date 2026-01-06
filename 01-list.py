server_1 = "172.31.7.183"
server_2 = "172.31.7.185"
servers = ["172.31.7.183", "172.31.7.185", 20,10 ]
print(type(servers))
print(servers[3])
print(servers[0:1])
# to print the servers in reverse
print(servers[-1:-5:-1])
#to find thelength of the server 
print("length of list:",len(server_2))
# list is a mutable data type
print("servers before modification:" ,servers)
servers[1] = 1000
print("servers after modification:" ,servers)
# to knw the which operations should perform on datatype
print("operations should perform on list:",dir(servers))

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
servers.append(1500)
print(servers)
# ['172.31.7.183', 1000, 20, 10, 1500]

# we can append list to the list
servers.append(["a","b"])
print(servers)

# ['172.31.7.183', 1000, 20, 10, 1500, ['a', 'b']]
# how to acces the value a

print(servers[-1][0])
a = ["a" ,"b"]
print(a)
# ['a', 'b']

a.extend(["c" ,"d"])
print(a)

# ['a', 'b', 'c', 'd'] 

a.append(["e","f"])
print(a)

#['a', 'b', 'c', 'd', ['e', 'f']]

print(a.index('c')) # 2

a.append('c')
print(a)
# ['a', 'b', 'c', 'd', ['e', 'f'], 'c']

print(a.index('c')) 
# if we want second c index
print(a.index( 'c', 2+1 ))

# "insert()" the value before the given index
a.insert(0,'x')
print(a)
#['x', 'a', 'b', 'c', 'd', ['e', 'f'], 'c']

# "remove()" the first occurance of the value
a.remove('c')
print(a)
# ['x', 'a', 'b', 'd', ['e', 'f'], 'c']

# reverse the list of values
a.reverse()
print(a)




