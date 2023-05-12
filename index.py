age = 18 
if age >= 18:
    print("You can drive motobike")
else: 
    print("You can't drive motobike")

num =  int(input("Nhập số nguyên: "))

if num > 0:
    print("Số này là số dương")
elif num == 0:
    print('Số này là số không')
else:
    print('Số này là số âm' )

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 == 0:
        print(num, "Even number")
    else:
        print(num, "odd")


a = 0
b = 0
if a - 1 < 0:
    print('a smaller than 1')
    if b - 1 < 0:
        print('b bigger than 1')

# Cả khối trên là một blog của if 


a = 3
if  a - 1 < 0: # False, tiếp tục    
    print('a is less than 1')
elif a - 2 < 0:
    print('a is less than 2')
elif a - 3 < 0:
    print('a is less than 3')
elif a - 4 < 0:
    print('a is less than 4')
elif a - 5 < 0:
    print('a is less than 5')
else:
    print("I don't know")


b = 4
if b - 1 < 0:
    print('b is less than 1')
else: 
    print('a is less than 5')


