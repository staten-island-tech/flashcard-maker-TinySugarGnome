""" def freeshirts():
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
freeshirts() """
def freeshirts():
    N, M, D = map(int, input().split())
    B = set(map(int, input().split()))  # event days where he gets a shirt

    shirts = N
    laundry_count = 0

    for day in range(1, D + 1):
        
        if shirts == 0:
            laundry_count += 1
            shirts += 1  # does laundry, gets 1 clean shirt
        shirts -= 1  # wears shirt
        if day in B:
            shirts += 1  # gets a new shirt from event

    print(laundry_count)
freeshirts()