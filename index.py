# Giới hạn bởi các cặp ngoặc vuông []
# Các phần tử của list cách nhau bởi dấu ,
# list chứa mọi giá trị của Python
# và bao gồm chính nó 

a = [ 1, "list", 2 , 5, "Convert", ["interface", "Name",], ["course Python"]]
print(a)

# list rỗng
b = [i for i in range(30)]
print(b)

c = [yushing for yushing in ("TypeScript")]
print(c)

d = [[n, n *1, n*2] for n in range(1,5)]
print(d)

a = [1,2]
a += ['one', 'two']
print(a)

j = [3,4]
b = 'Kteam' in a
print(b)

a = [1,2, 'a', 'b', 'c', [3,4]]
a[1] = 'guenfufun'
b = a[1]
print(b)
print(a)

a = [[1,2,3], [4,5,6], [7,8,9]]
print(a[0][-1])
print(a[1][1])
print(a[2][2])

l = [1,23,4,5,7]
p = l
print(l)
print(p)

p[0] = 'kteam'
print(p)
print(l)

a = [[1,2,3], [4,5,6]]
b = a
print(a)
print(b)

print("======")

r = [[1,2,3,45,6], [7,8,9,10]]
t = list(r)

print(r)
print(t)
t[0] = 'Yushing'
print(r)
print(t)



