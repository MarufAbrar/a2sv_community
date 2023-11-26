class Solution:
    def numIdenticalPairs(self, nums):
        numFreqMp = {}
        
        answer = 0
        for num in nums:
            answer += numFreqMp.get(num, 0)
            numFreqMp[num] = numFreqMp.get(num, 0) + 1
        return answer
