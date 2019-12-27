

a = 1
#print(a)



def dist(date:list):
    #elemtnts = set(date)
    #for v in date:
    #    elemtnts.add(v)
    return list(set(date))


def form_map(names, phone):
    name_to_phone = dict()
    for i in range(names):
        name_to_phone[names[i]] = phone[i]
    return name_to_phone

#print(form_map())

def format_date(date):
    part = date.split(".")
    m = int(part[1])
    if m is None:
        return "beeee"
    else:
        return m


try:
    pass
    #a = int(input())
    #b = int(input())
except ValueError as err:
    pass #print(err)
finally:
    pass #print(a + b)

try:
    file = open('test.txt', 'r')
    for i in file:
        print(i)
except:
    print("Err")
finally:
    if file is not None:
        file.close()

with open('test.txt','r') as file:
    for line in file:
        print(line, end='')
























