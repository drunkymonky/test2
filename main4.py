
#v = input("первое число")
#v1 = input("второе число")
#if isinstance(v,int):
#    v=int(v)
#print('result ', v+v1)

"""
n = 10

while n <=10:
    v1 = input()
    v2 = input()
    v3 = input()
    if isinstance(v1,str) or isinstance(v3,str) or isinstance(v2,str) == False:
        print("Error")
        break
    print(eval(str(v1)+str(v2)+str(v3)) )
    n +=1
"""
"""
r = []
print(r)

v = input().split()

if v[0] == "append":
    v.remove("append")
    v = [int(x) for x in v]

    print(v)
    print('MAX = ', max(v))
    print('MIN = ', min(v))

    v.sort(reverse=True)
    print()
    print(v)
"""

v = [123, 456]
result = ""

v = [str(x) for x in v]
for x in v:
    result = '+'.join(list(x))
    print(eval(result))
    








