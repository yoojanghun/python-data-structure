from listByClass import ArrayList

L = ArrayList(50)

print(L)

L.insert(0, 10)
L.insert(0, 20)
L.insert(1, 30)
L.insert(L.size, 40)
L.insert(2, 50)
print(L)

L.replace(2, "hello")
print(L)