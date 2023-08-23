def decreasingStack(arr, N):
    stk = []

    for i in range(N):
        if (len(stk) > 0) and (stk[len(stk)-1] < arr[i]):
            stk.pop()
        stk.append(arr[i])

    N2 = len(stk)
    arr2 = [0]*N2
    j = N2 - 1

    while (len(stk) != 0):
        arr2[j] = stk[(len(stk)-1)]
        stk.pop()
        j = j - 1

    print("Your initial stack: ")
    for i in range(N):
        print(arr[i], end=", ")
    print()

    print("Your monotonic decreasing stack: ")
    for i in range(N2):
        print(arr2[i], end=", ")


arr = [24, 52, 30, 25, 43, 25, 10]
N = len(arr)

decreasingStack(arr, N)

# define function
# initialize stack
# create loop to make decrease/increase stack
# create variables to 1) store stack length, 2) store stack variables, 3) store it in proper order (can only retrieve informaton from top of stack (LIFO))
# create loop to empty stack and store stack information
# resulting: emptied stack and new variable that contains stack information
# display information
