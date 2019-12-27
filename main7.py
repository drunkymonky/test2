import time

def action():
    return (x for x in range(100000))

start_time = time.time()
action()
end_time = time.time()

print(end_time-start_time)


