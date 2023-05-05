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


# Hàm count đếm xem số lần xuất hiện của 1 phần tử là bao nhiêu lần 
a = [1,1,2,2,2,3,4,5,6,7]
c = a.count(1) 
print(c)

money = [60]
money_all = money

print(money)
print(money_all)

print ("======")

money_all.clear()

print(money)
print(money_all)

a = [1,2,3,4,5]
a.append([6,7])
print(a)

a.extend([6,7])
print(a)

#insert (Thêm phần tử, vào vị trí) 
a = [1,2,3]
print(a)
a.insert(4,4)
print(a)

print("=====")

#Pop Lấy ra phần tử và trả về phần tử đã lấy
a = [10,11,12]
c = a.pop(2)

print(a)
print(c)

n = [1,2,8,9,4,5]
n.remove(2)
print(n)
n.reverse() # Đảo ngược lại
print(n)

# sort sắp xếp từ bé đến lớn và đảo ngược theo key
n.sort()
print(n)
