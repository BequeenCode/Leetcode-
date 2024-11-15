from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array first
        result = []  # To store the unique triplets
        
        # Iterate through the array with the first pointer
        for i in range(len(nums) - 2):
            # Skip duplicate elements to avoid repeating the same triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])  # Found a triplet
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1  # We need a larger sum, move the left pointer
                else:
                    right -= 1  # We need a smaller sum, move the right pointer
        
        return result
