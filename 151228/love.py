#-*- coding: utf-8 -*-

heart = 0

print "여자 : 반갑다."
print "나 : 나도 반갑다."

x = int(raw_input("여자에게 칭찬을 하시려면 1을, 험담을 하시려면 2를 눌러주세요."))
if x == 1:
    print "나 : 너 정말 예쁘다."
    print "여자 : 고맙다 너도 잘생겼어"
    heart += 1
else:
    print "나 : 근데 너 못생겼다."
    print "여자 : 어 너도"
    heart -= 1

x = int(raw_input("여자에게 명품을 사주려면 1을, 안 사주려면 2를 눌러주세요."))
if x == 1:
    print "나 : 오다 주웠다. 루이비똥이다."
    print "여자 : 이런거 너무 부담스러워..."
    heart -= 1
else:
    print "나 : 너에게 줄 건 아무 것도 없다."
    print "여자 : 너 정말 박력있다"
    heart += 1

print "나 : 이제 우리 사귀는 사이가 되는 건 어떨까?"
if heart > 1:
    print "여자 : 그래 그럼 오늘부터 1일!"
    print "Game Clear"
else:
    print "여자 : 내가 미쳤냐 너랑 사귀게"
    print "Game Over"
