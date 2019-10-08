class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

#Brute Force
        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums):
                if (nums[i] == target - nums[j]) and (i!=j):
                    return [i,j]
                else:
                    j = j+1
            i = i+1
            
#Use Dict

    dict = {}
    for index, num in enumerate(nums):
        number = target - num
        if number not in dict:
            #so the data in dict looks like {num:index}
            dict[num] = index
        else:
            return [dict[num], index]
            
    