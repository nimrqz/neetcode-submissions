class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valores = len(list(set(nums)))!=len(nums)
        return  valores
        # visto = set()
        # for num in nums:
        #     if num in visto:
        #         return True
        #     visto.add(num)
        # return False