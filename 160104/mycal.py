# my calculation

def my_add(first, second = 1):
    result = first + second
    return result

def my_sub(first, second):
    result = first - second
    return result

def my_mul(first, second):
    result = 0
    for x in range(0, second):
        result += first
    return result

def my_div(first, second):
    if type(first) == float or type(second) == float:
        print "integer only"
        return

    result = 0
    while first >= second:
        result += 1
        first -= second

    return result

def my_add2(*nums):
    print nums
    result = 0
    for n in nums:
        result += n
    return result

def my_thing(**thing):
    print thing
    for k, v in thing.items():
        print v, "in my", k

my_thing(left_pocket = "cellphone", right_pocket = "nothing")
my_add2(1,5,4,6)
result = my_sub(second = 5, first = 7)
print result
