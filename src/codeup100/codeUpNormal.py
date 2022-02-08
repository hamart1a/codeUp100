#짝수 합 구하기
def codeUp77():
    #값을 입력받는다.
    print("값을 입력받습니다.")
    num = int(input())
    total = 0
    cnt = 1
    #더하는 작업을 반복한다.
    while cnt <= num:
        #짝수인지 홀수인지 검사한다.
        if cnt % 2 == 0 :
            total += cnt
        cnt += 1
    return print(total)

def codeUp77_1():
    print("값을 입력받습니다.")
    num = int(input())
    total = 0
    for i in range(1,num+1):
        if i % 2 == 0 :
            total += i
        i += 1
    return print(total)

def codeUp79():
    print("값을 입력받습니다")
    num = int(input())
    lastNum = 1
    cnt = 1

    while lastNum < num :
        cnt = cnt + 1
        lastNum = lastNum + cnt
    return print(cnt)

def codeUp82():
    print("값을 입력받습니다")
    num = int(input())
    cnt = ""
    result = ""

    for i in range(1,num+1):
        #10으로 나눠서 나머지가 3, 6, 9
        q = i / 10
        r = i % 10
        if r == 3 or r == 6 or r == 9:
            cnt = "X"
            #몫이 3,6,9 면 짝짝
            if q == 3 or q == 6 or q == 9:
                cnt + "X"
        else : cnt = str(i)
        result += cnt+ " "
    return print(result)

def codeUp83():
    print("값을 입력받습니다")
    # rgb = input()
    # r,g,b = rgb.split(" ")
    r,g,b = map(int, input().split())
    cnt = 0
    
    for i in range(0,int(r)):
        for j in range(0,int(g)):
            for k in range(0,int(b)):
                print(i,j,k);
                cnt = cnt + 1
    print(cnt)

def codeUp84():
    #print("값을 입력받습니다")
    h,b,c,s = map(int, input().split())
    res = round(h * b * c * s /8/1024/1024,1)
    print(str(res)+" MB")

def codeUp85():
    #print("값을 입력받습니다")
    n = int(input())
    cnt = 0
    res = 0
    while res < n:
        res = res + cnt
        cnt += 1
    print(res)





