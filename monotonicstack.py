def increasingStack(arr, N):
	stk=[] #initialize the stack
	
	for i in range(N): #while length of stack is greater than 0 and the last element of stack is greater than array index - pop off. 
		while(len(stk) > 0 and stk[len(stk) - 1] > arr[i]):
			stk.pop()
		stk.append(arr[i])
	
    #appends the new element when it is greater than the top of the stack.
		
    
		
	N2 = len(stk) #length of finished appending stack
	ans = [0]*N2 #initialize new stack length = to [0]*N2 = [0,0,0]
	j = N2 - 1 #used to go through the stack backwards.
	
	while(len(stk) != 0):
		ans[j] = stk[len(stk) - 1] #replaces index:value of new stack with index:value of finished stack
		stk.pop() #pops value from stack
		j = j - 1 #repeat until stack is empty.
	
	
	print("The Array: ",end="")
	for i in range(N): #prints out the array.
		print(arr[i],end=" ")
	print()
	
	
	
	print("The Stack: ",end="")
	for i in range(N2):
		print(ans[i],end=" ") #prints out the index of new stack ans.
	
# Driver code
arr = [1, 4, 5, 3, 12, 10]
N = len(arr)

# Function Call
increasingStack(arr,N)

# This code is contributed by Pushpesh Raj.
