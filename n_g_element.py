def next_greater_element(nums):
    stack = [] #intialize the stack
    result = [-1] * len(nums) # [-1,-1,-1/..len(nums)]
     
    for i in range(len(nums)): #itirate over length of nums
        while stack and nums[i] > nums[stack[-1]]: #while stack and index nums is greater than last element of the stack
            index = stack.pop() #new variable with value of popped index 
            result[index] = nums[i] #result [2] = nums [i]
        stack.append(i) #append i to stack
     
    return result
 
# Example usage
nums = [4, 5, 2, 25, 7, 18]
result = next_greater_element(nums)//
print("Input Array: ", nums)
print("Next Greater Elements: ", result)



