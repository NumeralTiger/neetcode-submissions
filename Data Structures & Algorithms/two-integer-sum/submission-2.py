class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i , n in enumerate(nums):
            if target - n in num_map:
                num2 = target - n
                idx2 = num_map[num2]
                return [idx2 , i]
            else:
                num_map[n] = i