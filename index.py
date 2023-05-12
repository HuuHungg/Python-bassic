k = 5
while k > 0:
    print('K = ', k)
    k -= 1

s = 'How Kteam'
idx = 0 # Vị trí bắt đầu muốn xử lý chuỗi
length = len(s) # Lấy độ dài chuỗi làm mốc kết thúc
while idx < length:
    print(idx, 'stands for', s[idx])
    idx += 1

# BREAK 
five_even_numbers = []
k_number = 1

while True:
    if k_number % 2 == 0:
        five_even_numbers.append(k_number)
        if len(five_even_numbers) >= 5:
            break
    k_number += 1

print(five_even_numbers)
print(k_number)

print("=======")

# Continue
k_number2 = 0
while k_number2 < 10:
    k_number2 += 1
    if k_number2 % 2 == 0: # Nếu in ra những số chẵn thì nó sẽ bỏ qua và tiếp tục in 
        continue
    print(k_number2, "is odd number")

print(k_number2)

k = 0
while k < 3:
    print('value key is of ',k)
    k += 1
    if k == 2:
        break
else: 
    print('K is not less than 3 anymore')

