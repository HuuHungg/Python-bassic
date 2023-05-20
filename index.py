yushing = lambda x : x**2

result = yushing(5)
print(result)

number = [1,2,3,4,5,6]
squared_numbers = list(map(lambda x: x**2, number))
print(squared_numbers)


def total(a,b,c):
    return(a + b + c)/3
print(total(4,5,6))

yushing2 = lambda a,b,c : (a + b + c)/3
print(yushing2(7,8,9)) 

x_power_a = lambda x,a=2 : x ** a
print(x_power_a(4))

def yushing3():
    mem = lambda x : x + 'is a member of fullName GuEn Yushing'
    return mem

call_me = yushing3()
print(call_me('毎日ITを勉強二時間ぐらいするつもりです'))

print("==== + =====")

yushing_list= [lambda x : x ** 2, lambda x: x ** 4, lambda x: x ** 5]
for func in yushing_list:
    print(func(3))

find_greater = lambda x,y : x if x > y else y
print(find_greater(1,2))

cd_of_2_3 = lambda x : (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
print(cd_of_2_3(6))

def kteam(first_string):
    return lambda secound_string: first_string + secound_string
slogan = kteam('毎日ITを勉強してる')

addition = lambda a,b : a + b + '毎日ITを勉強してる頑張りましょうでも今日は頭が痛いです'
print(addition("お名前","は"))