class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
                for j in nums:
                    if j == i:
                        d[i] += 1
        return max(d, key=d.get)