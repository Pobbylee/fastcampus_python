# coding=utf-8
# 성적을 입력하여 평균을 내는 프로그램입니다

total = 0
count = 0

while count < 5:
    grade = int(raw_input("Enter grade: "))
    total = total + grade
    count += 1

avrg = float(total) / 5 # 하드코딩

# 학급 평균 출력
print "Class average is " + avrg
