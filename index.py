def sum(a,b):
    result = a + b
    return result
print(sum(2,3))


def yushing(a,b):
    print("毎日ITを勉強してる頑張りましょう")
    return a + b

print(yushing("でもITが難しいですが", "頑張ってください"))

def kteam(text,age):
    print(text)
    print(age)

kteam(" Hello Kteam !", 69)
kteam("毎日ITを勉強してるでもに日本語勉強した午後を食べました", 60)
kteam("頭が痛いですら", 45) 


def yushing2(age, name="yushing"):
    print(age)
    print(name)
yushing2(21)
yushing2(60, "yushing2")


def f(yushing3 = []):
    yushing3.append('H')
    yushing3.append('T')
    print(yushing3)

f()
f()
f()
f()




def add_number(x,y):
    return x + y

print(add_number(2,3))


def total_sum (a,b = 2, c = 3, d = 4):
    f = (a + d ) * (b + c)
    print(f)

total_sum(1, d = 4)

def yushing5(pos_or_key, key_arg_1, key_arg_2):
    print(pos_or_key)
    print(key_arg_1)
    print(key_arg_2)

yushing5(pos_or_key="毎日ITを勉強している", key_arg_1="２時間ぐらい", key_arg_2="難しいです")


# Diện tích hình chữ nhật
def recatangle_area(width, height):
    return width * height
area = recatangle_area(7,10)
print(area)

def print_info(name, age, gender):
    print("Tên", name)
    print("Tuổi", age)
    print("Giới tính", gender)

print('John', 21, "Nam")

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

reusult = find_max([1,2,3,4,5,6,7,8,9,10,11,12,13,15,16])
print(reusult)


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = sum_list([1,2,3,4,5,6])
print(result)


def is_prime(n):
    if n in [2,3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))

def evenOdd(x):
    if(x % 2 == 0):
        print("event")
    else:
        print("odd")

evenOdd(2)
evenOdd(3)