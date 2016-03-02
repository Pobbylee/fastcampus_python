# recursive function using recursion

def factorial(num):
    if num == 1:
        return 1

    return num * factorial(num - 1)

result = factorial(5)
print result
