# Sorting Algorithms
# Insertion Sort
nums=[64,32,25,45,40,51,2] 
def InsertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key    
    print(nums)
InsertionSort(nums) 
#print(nums)   