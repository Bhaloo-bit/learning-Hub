# bubble sorting
# time complexit  order(n^2)

def bubbleSort(nums):
   n = len(nums)

   for i in range(n):
      for j in range(0, n-1-i):
         if (nums[j] > nums[j+1]):
            nums[j],nums[j+1] = nums[j+1], nums[j]


nums=[64,32,25,45,40,51,2]  
bubbleSort(nums)  
print(nums)

