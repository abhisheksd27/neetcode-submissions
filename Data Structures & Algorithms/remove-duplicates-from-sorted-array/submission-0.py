class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        i = 0  # slow pointer
        j = 1  # fast pointer
        
        while j < len(nums):
            if nums[j] != nums[i]:  # new unique number found
                i += 1              # move slow pointer
                nums[i] = nums[j]   # copy unique number
            j += 1                  # always move fast pointer
        
        return i + 1
