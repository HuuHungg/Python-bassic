a = "毎日ITを勉強してる頑張りましょう"
b = "でも難しいですが家族から"
c =  "毎週８０時間ITと日本語と英語勉強します"


print(a + b + c)


my_string = " This is a sample string in my class room"
my_list = my_string.split()
print(my_list)


my_string = "apple,banana,orange,grape"
my_list = my_string.split(",")
print(my_list)

a = "I am  learning English width my friend end my family"
b = a.split(' ', 2)

print(a)
print(b)

c = "how kteam free education "
d = c.rpartition("kteam")
print(c)
print(d)

e = "how kteam education interface on spacebetween and my wife"
f = e.startswith('h')
print(f)

g = "Hello world"
h = g.find("w")
print(h)

#isdigit() giúp kiểm tra xem thằng này có phải là số không
a = "5a" 
b = a.isdigit()
print(a)
print(b) 

print("=======")

#isspace: Kiểm tra xem có khoảng trắng không
a = '  '
b = a.isspace()
print(b)


