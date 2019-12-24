

"""
# !!!!!
result = [x+y for x in range(10) for y in range(10)]
print(result)

# !!!!!

a = 12
b = 23

max = b if b > a else a # тернарный ОПЕРАТОР





a = 10
b = 20
v = [x ** 2 for x in range(a,b+1)]
#print(v)

v = [x * 2 for x in v if x % 2 == 0]
#print(v)

v = [100 if x < 200 else 400 for x in v]
#print(v)


#1
a = 3
b = 7
v =[x for x in range(a,b+1)]
print(v)

#2
n = 32
v = [2**x for x in range(n)]
print(v)

#3
v  = 'bcDFRds'
v = [x for x in v if x.isupper()]

print(v)

#4
a = [
     [1,2,3],
     [3,5,4],
     [6,7,9]
    ]
print(a[1][2])

n= 4
m = 5
data = [[0 for y in range(m)] for i in range(n)]
print(data)

for r in data:
    for e in r:
        print(e, end=', ')
    print()

#5

n = 5
v = [[x*y for y in range(n)] for x in range(n)]
print(v)


"""
# 6
n=5
f = [[0 for i in range(n)] for j in range(n)]

f[0][1] = 'x'
f[2][3] = 'x'
f[2][1] = 'x'

x = 1
y = 1

f.insert(0,[0]*7)
f.append([0]*7)

for i in range(1,n+1):
    f[i].append(0)
    f[i].insert(0,0)
    

x+=1
y+=1
bomb_count = 0

for i in range(-1,2):
    for j in range(-1,2):
        if f[x+i][y+j] == 'x':
            bomb_count += 1

#print(bomb_count)
#print(f)

result = []
n = 4

for i in range(n):
    current_list = [x for x in range(n*i+1, n*(i+1)+1)]
    if i % 2 == 1:
        current_list.reverse()
    result.append(current_list)

#print(result)

# 7
x = 0
y = 0
dir = 0
n =3
result = [[0 for i in range(n)] for j in range(n)]
i = 1
while i < n* n:
    
for row in result:
    print(row)


print(result)









"""
#6
v = [
    [0,-1,0]
    [0,0,0 ]
    [-1,0,0]
    ]
"""













