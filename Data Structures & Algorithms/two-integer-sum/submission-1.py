class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for n, i in enumerate(nums):
            index[i] = n
        
        for a, b in enumerate(nums):
            c = target - b
            if c in index and index[c]!= a:
                return [a, index[c]]

            
