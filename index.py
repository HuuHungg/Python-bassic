a = 'Kteam'
b = id(a)

print(b)
print(id("Kteam"))

n = 69
print(n)
print(n * 2)
print(n.__mul__(2))

s_1 = "HowKteam" 
s_2 = 'Free education'

s_1 = s_1 + 'Python'
s_2 += 'Python'

print(id(s_1))
print(id(s_2))

print("=====")

s_3 = [1,2]
print(id(s_3))

s_3 = s_3.__add__([3,4])
print(id(s_3))

print("====")
s_4 = [1,2,3]
s_4.append(4)

print(s_4)

s_5 = (1,2,3,4,5)
s_5 += (6,7)
print(s_5)