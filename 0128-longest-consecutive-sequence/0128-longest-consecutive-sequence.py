class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        ls =1
        n=1
        for i in range(1,len(nums)):
            if nums[i]- nums[i-1] == 1 :
                n+=1
            else:
                if n>ls:
                    ls = n
                n = 1
        return max(ls,n)     
        