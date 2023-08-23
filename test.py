def decreasingstack(arr, N):
    stk = []

    for i in range(N):
        while(len(stk) > 0 and stk[len(stk)-1]<arr[i]):
            stk.pop()
        stk.append(arr[i])
    
    N2 = len(stk)
    array2 = [0]*N2
    j = N2 - 1

    while (len(stk)!=0):
        array2[j] = stk[len(stk)-1]
        stk.pop()
        j = j - 1
    
    print("Your Initial Array: ")
    for i in range(N):
        print(arr[i], end=" ")
    print()


    print("Monotonic Decreasing Array: ")
    for i in range(N2):
        print(array2[i], end=" ")


arr = [0, 1, 2, 5, 10, 19, 24, 18, 14, 15, 20, 4, 3]
N = len(arr)

decreasingstack(arr, N)