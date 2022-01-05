## 09. 입력

# c = input()
# print(c)

## 10. 형변환

# n = input()
# n = int(n)
# print(n+1)

## 날짜 순서 바꾸기(split)

# y, m, d = input().split('.')
# print(d+'-'+m+'-'+y)

## 주민번호(replace)

# num = input().replace('-', '', 1)
# print(num)

## 분만 출력(split)

# h, m, s = input().split(':')
# print(m)

## 2진수 -> 16진수

# num = input()
# n = int(num)
# print('%x' % n) #소문자 형태 16진수 문자열
# print('%X' % n) #대문자 형태 16진수 문자열

##16진수 -> 8진수

def codeUp29():
    a = input()
    n = int(a, 16)
    print('%o' % n)
    return;


## 영문자 -> 유니코드

# n = ord(input())
# print(n)

## c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다.
# c = int(input())
# print(chr(c))

# 실수 계산
def codeUp35():
    f1, f2 = input().split()
    m = float(f1) * float(f2)
    print(m)
    return


# 문자열 반복 출력
def codeUp37():
    n = input()
    s = input()
    print(int(n + " ") * s)
    return


# 거듭제곱
def codeUp38():
    a, b = input().split()
    c = int(a) ** int(b)
    print(c)
    return


# 나머지 계산
def codeUp41():
    a, b = input().split()
    print(int(a) % int(b))
    return

#소숫점 자리 변환
def codeUp42():
    a = float(input())
    print(format(a, ".2f"))
    return

#비트연산 and
def codeUp60():
    a,b = input().split()
    print(int(a) & int(b))
    return

#삼항연산
def codeUp64():
    a,b,c = input().split()
    a = int(a) # split시 문자열로 처리됨
    b = int(b)
    c = int(c)
    d = (a if a < b else b)
    print(d if (d < c) else c)
    return

#반복문
def codeUp74():
    c = ord(input()) #ord -> char정수값
    t = ord('a')
    while t <= c:
        print(chr(t), end=' ')
        t = t+1
    return