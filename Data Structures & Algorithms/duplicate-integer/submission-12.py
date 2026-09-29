class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        
        #return len(list(set(nums)))!=len(nums)

        # visto = set()
        # for num in nums:
        #     if num in visto:
        #         return True
        #     visto.add(num)
        # return False