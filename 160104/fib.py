mem = [0, 1]

def fib1(num):
    a0 = 0
    a1 = 1
    a2 = None

    if num == 1 or num == 2:
        return 1

    for x in range(2, num):
        a0 = a1
        a1 = a2
        a2 = a0 + a1

    return a2

def fib2(num):
    if num == 1 or num == 2:
        return 1

    return fib2(num - 1) + fib2(num - 2)

def fib3(num):
    if len(mem) > num:
        return mem[num]

    mem.append(fib3(num - 1) + fib3(num - 2))
    return mem[num]

print fib1(20)
print fib2(20)
print fib3(20)
