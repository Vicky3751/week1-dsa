class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqDict = Counter(nums)
        size = len(nums)
        for (key,val) in freqDict.items():
            if (val > (size/2)):
                return key
        
