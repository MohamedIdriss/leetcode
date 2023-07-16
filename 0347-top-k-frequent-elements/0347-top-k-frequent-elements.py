

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        ncount = {}
        count = 1
        nums.sort()
        for i in range(0,len(nums)-1):
            if(nums[i] == nums[i+1]):
                count +=1
            else:
                ncount[nums[i]] = count
                count = 1
        ncount[nums[-1]] = count
        
        frequent_elements = heapq.nlargest(k, ncount.keys(), key=ncount.get)
        return frequent_elements
            
        
    
