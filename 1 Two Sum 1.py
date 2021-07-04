class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        
        for i, elem1 in enumerate(nums):
            for j, elem2 in enumerate(nums):
                if i != j and elem1 + elem2 == target:
                    a.append(i)
                    
        return a
