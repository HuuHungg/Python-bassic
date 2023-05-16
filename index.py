# while
k = 0
while k < 5:
    print("I am coding run", k)
    k += 1


s = "Yushing"
idx = 0
length = len(s)

while idx < length :
    print(idx,"start for code run", s[idx])
    idx += 1

print("=====")

# Break

five_even_numbers = []
k_number = 1


five_number = []
y_number = 1

while True:
    if y_number % 2 == 0:
        five_number.append(y_number)
        if len(five_number) >= 5:
            break
    y_number += 1

print(five_number)
print(y_number)


k_number = 0
while k_number < 10:
    k_number += 1
    if k_number % 2 == 0:
        continue
    print('K is number odd', k_number)


k = 0
while k < 5:
    print('Value key is of', k)
    k += 1
    if k == 2:
        break
else:
    print('K is not less than 3 anymore')