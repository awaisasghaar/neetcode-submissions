class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        else:
            return False


# Time complexity: O(nlogn)
# Space complexity: O(1) or O(n) depending on the sorting algorithm used
        