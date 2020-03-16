#-- 28.85% ...
# memory is not linear

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums)%2==0:
        #     return -1
        c = Counter(nums)
        return c.most_common()[-1][0]