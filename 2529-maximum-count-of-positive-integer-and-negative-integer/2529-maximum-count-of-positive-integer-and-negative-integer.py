class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        zeroCnt = 0
        negCnt = 0
        
        for num in nums:
            if num < 0:
                negCnt += 1
            elif num == 0:
                zeroCnt += 1
            else:
                break

        return max(negCnt, len(nums)-negCnt-zeroCnt)