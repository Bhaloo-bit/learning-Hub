# selection sorting
# time complexity O(n^2)
nums=[64,32,25,45,40,51,2] 

def selectionSort(nums):  # increasing order itrations
    n = len(nums)
    for i in range(n):
        min = i
        for j in range(1,n):
            if (nums[min] > nums[j]):
                min = j
        nums[i],nums[min] = nums[min], nums[i]        

            
selectionSort(nums)
print(nums)