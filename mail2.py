

print(ord('a'))

s = 'B'

print(chr(ord(s) + 32))


s = 'Hello'

print(s.upper())
res = ""
for i in s:
    if i <= 'Z':
        res += i.lower()
    else:
        res += i.upper()

print(res)


l = [1,2,3,4,5]

for i in range(1,len(l)-1):
    if l[i] < l[i+1]:
        #print("yes")
        pass
    else:
        print("no")
        break





















