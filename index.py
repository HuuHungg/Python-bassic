# Sep: Chia ra, phân ra, trong Python 

print('Yushing', 'Python', 'Interface', 'Golang')
print('Yushing', 'Python', 'Interface', 'Golang', sep='|||')


# end Kết thúc 
print('a line without newline', end = '|||')

from time import sleep # nhập hàm sleep từ thư viện time vào
print("====")
print('start....')
sleep(1)
print('end....')

#flush xuất ra những gì có trong bộ nhớ đệm 

print('line 1\n', 'line2', end= '', flush=True)
sleep(3)
print('end...')


# Tạo ra file
with open ('printtext.txt', 'w') as f:
     print('Yushing learn English and IT with my frend and my family', file=f)
     print('毎日ITを勉強してる頑張りましょう', file=f)


your_name = "Yushing"
your_great = "Hello, My name is "

for c in your_great + your_name:
    print(c, end = '', flush=True)
    sleep(0.1)
print()

print('毎日二時間ぐらいITを勉強してる頑張りましょう')