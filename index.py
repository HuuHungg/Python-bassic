#Set được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là phần tử của Set
# Các phần tử của Set được phân cách nhau bởi dấu ,
# Set không chứa nhiều hơn 1 phần tử 

set_1 = {96,69}
print(set_1)

set_2 = {("How K team"), (1,2,3,4,5)}
print(set_2)

set_3 = {'HowKteam', "Kteam", 69}
print(set_3)

set_4 = {value for value in range(5)}
print(set_4)
print(type(set_4))

set_5 = set("Yushing")
print(set_5)
print(type(set_5))

print( 1 in {1,2,3,4})

print({1,2,3,4} - {3,4})

# &: Chỉ lấy thằng mà cả hai thằng đều có
print({1,2,3,4,5} & {3,4,5})

# | Lấy hế các phần tử của cả hai thằng 
print({1,2,3} | {5})

print("======")
set_1 = {1,2,3,4,5}
set_2 = {5,6}

set_3 = set_1 & set_2
set_4 = set_1 | set_2
set_5 = set_4 - set_3

print(set_3)
print(set_4)
print(set_5) 

# Các phương thức của set 
#Pop lấy ra thằng đầu tiên 

set_6 = {9,10,11,12,13,14}
set_6.pop()
set_6.remove(10)
print(set_6)

#discard nếu như value không có thì nó sẽ bỏ qua
set7 = {"yushing", "name", "PHP", "Ruby", "Interface"}
set7.discard("find") #Nếu không có value thì nó sẽ bỏ qua
set7.remove("name")
print(set7)

print("=====")

set8 = set7.copy()
set8.add("Japanses")
print(set8)

set9 = {1,2,3,4,5}
print(set9)
set10 = set9
set10.clear()
print(set10)
