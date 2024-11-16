class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        i = 0
        j = 0
        while j <size:
            if i<=j and nums[i]== nums[j]:
                j +=1
            elif i<j and nums[i]!=nums[j]:
                nums[i+1] = nums[j]
                i +=1
                j +=1
      
        return i+1