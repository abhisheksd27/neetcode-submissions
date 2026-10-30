class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i=0
        j=len(numbers)-1

        while i<j:
            if numbers[i]+numbers[j]>target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                return [i+1,j+1]