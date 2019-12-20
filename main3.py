


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
#6
v = [
    [0,-1,0]
    [0,0,0 ]
    [-1,0,0]
    ]
"""













