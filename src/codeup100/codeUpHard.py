

def codeUp91():
    a,b,c = map(int,input().split())
    d=1
    while d%a!=0 or d%b!=0 or d%c!=0 :
        d +=1
    print(d)


def codeUp92():
    n = int(input())
    calls = input().split()
    callCntArr = []
    for i in range(24):
        callCntArr.append(0)


    for j in range(n):
        call = calls[j]
        call = int(call)
        callCntArr[call] += 1

    for k in range(1, len(callCntArr)):
        print(callCntArr[k],end=' ')


