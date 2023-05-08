file_object = open('Yushing.txt')
data = file_object.read()
file_object.close()
file_object = open('Yushing.txt')
data2 = file_object.read()
print(data)
print(" ===== ")
print(data2)

# Phương thức readline là đọc từng dòng
data = file_object.readline()
data2 = file_object.readline()
file_object.close()
print(data)
print(data2)



