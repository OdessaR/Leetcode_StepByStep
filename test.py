nums = [0,1,0,3,12]
pos = 0
        
for i in range(len(nums)):
    el = nums[i]
    if el != 0:
        nums[pos], nums[i] = nums[i], nums[pos]
        print(nums)
        pos +=1


j = 1
k = 2
j, k = k, j
print(j,k)