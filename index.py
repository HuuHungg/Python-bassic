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
