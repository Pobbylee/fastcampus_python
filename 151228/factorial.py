# coding=utf-8

num = int(raw_input("Enter number: "))
result = 1

cnt = num
while cnt > 1:
    result *= cnt
    cnt -= 1

print str(num) + "! is " + str(result)
