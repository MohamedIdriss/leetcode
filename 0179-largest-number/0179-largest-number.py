class Solution:
    def largestNumber(self, nums: List[int]) -> str: 
        k = 0
        for i in range(0,len(nums)):
            k=k+nums[i]
            nums[i] = str(nums[i])
        if k == 0:
            return "0"
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] < nums[j]+ nums[i]:
                    x = nums[i]
                    nums[i] = nums[j]
                    nums[j] = x

        return "".join(nums)