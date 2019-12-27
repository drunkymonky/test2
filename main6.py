
import datetime
from audioop import avg
from statistics import mean 

def EOMonth(mon):
    if mon == 2:
        return 28
    elif mon in (1,3,5,7,8,10,12):
        return 31
    else:
        return 30

weather = dict()
month = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
for i in range(len(month)):
    weather[month[i]] = [0] * EOMonth(i)

print(weather['jan'])

with open("data_one_year.txt", 'r') as file:
    for m in weather:
        for i in range(len(weather[m])):
            weather[m][i] = int(file.readline())


while True:
    inp = input().split()
    command = inp[0]

    if command == 'temp':
        print(weather[inp[1]][inp[2]])
    if command == 'avarege':
        if inp[1] == 'year':
            s = 0
            for i in weather:
                s += sum(weather[i]) / len(weather[i])
            print(round(s,2))
        else:
            print(sum(weather[inp[1]]) / len(weather[inp[1]]))
    
import time












