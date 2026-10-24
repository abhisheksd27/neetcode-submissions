class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        res, maxCount=0,0
        for i in nums:
            count[i] =1+ count.get(i,0)
            res= i if count[i] > maxCount else res
            maxCount=max(count[i],maxCount)

        return res
