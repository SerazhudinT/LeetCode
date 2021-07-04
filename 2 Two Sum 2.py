class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = ()

        for i in range(len(nums)):
            if target - nums[i] in numsSet:
                break
            else:
                numsSet.add(nums[i])

        for j in range(i):
            if nums[j] == target - nums[i]:
                break

        return j, i
