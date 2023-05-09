itera = (x for x in range(3))
print(itera)
print(sum(itera,2))
print(max (9,5,25,6))
print(max([], default = "Yushing"))

itera2 = [1,2,7,9,6,4,3]
print(itera2)
print(sorted(itera2))
print(sorted(itera2, reverse=True))

numbers = [1,2,3,4,5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

string = 'Hello, world in the Python'

for char in string:
    print(char)

print(123, [4,5,6], 'Kteam')