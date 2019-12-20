

d = [-2, 3, -5, 4, 65]
# -- 1
n= 0
for i in d:
    if i > 0:
        n+=1
print('1 -- ', n)

                         

# -- 2
for i in d:
    if (i % 2) == 0:
        print('2 -- ',i)


#3 --
print('3 -- ', d[::2]. )

#4
print('4 -- ',sum(d)/len(d))

#5
for i in d:
    if len(i) > 5:
        print('5 -- ', i)