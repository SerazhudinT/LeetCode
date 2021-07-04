class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            if numsDict.get(target - nums[i]) != None and numsDict[target - nums[i]] != i:
                return numsDict[target - nums[i]], i
            
            numsDict[nums[i]] = i
