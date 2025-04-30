def freeshirts():
    N,M,D = map(int,input.split())
    B = list(map(int,input().split()))
    B.sort()
    laundary = D - N
    for i in range(D+1):
        if M != len(B):
            print('noonononon')
        elif i not in range(D+1):
            laundary -= i
    print(laundary)
freeshirts()