# coding=utf-8
# 팩토리얼을 for 문으로!

num = int(raw_input("Enter number: "))
result = 1

for cnt in range(2, num + 1):
    result *= cnt

print str(num) + "! is " + str(result)
