class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            if f"{nums[i]}" in dic:
                return True
            else:
                dic.update({f"{nums[i]}":nums[i]})
        return False