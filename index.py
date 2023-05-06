dic =  {'name': 'Kteam', 'member': 69}
print(dic)
print(type(dic))

dic = {key: value for key, value in [('name', 'kteam'), ('member', 69)]}
print(dic)
print(type(dic))

iter_ = [('name', 'Yushing'), ('member', 21)]
dic = dict(iter_)
print(dic)
print(type(dic))


dic = dict(name = 'Kteam', member = 69, FE = "Free education")
print(dic)
print(type(dic))

iter_ = ('name', 'number','age', 70, True)
dict = dict.fromkeys(iter_, "Yushing ")

dict['name'] = 'ぐえんフフン'
print(dict['name'])

# khi thêm một cặp key và value
dict ['addRed'] = 'Free Education'
print(dict)

print("=====")

dic = dict(K = 60, HK = "Yushing", AGE = 80)
print(dic)

dic['K'] = dic['K'] + 1
print(dic)

dic = dict(K = 'Kteam', HK = "HowKTeam", FE = 'Free education')
print(dic)

dic['K'] = dic['K'] + ": I am leaning English with my friend"
print(dic)