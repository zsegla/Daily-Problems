# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/



class Solution:
    def solve(self, nums, d, p):
            n = len(nums)
            c = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= d:
                    c += 1
                    i += 1
                if c >= p:
                    return True
                i += 1
            return False
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        lo, hi = 0, nums[n - 1] - nums[0]
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if self.solve(nums, mid, p):
                hi = mid
            else:
                lo = mid + 1
        return lo
