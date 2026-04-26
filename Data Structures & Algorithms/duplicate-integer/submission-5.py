'''Brute Force approach'''

# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False

# '''TIME COMPLEXITY: O(N^2)'''
# '''SPACE COMPLEXITY: O(1)'''

'''Sorting approach'''
# class Solution:
#     def hasDuplicate(self, nums: list[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1]:
#                 return True
#         return False

# '''TIME COMPLEXITY: O(nlogn)'''
# '''SPACE COMPLEXITY: O(1)'''

'''HASH SET'''
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return True
            
            nums_set.add(num)
        return False

# Time Complexity: O(n)
# Space Complexity: O(n)
      