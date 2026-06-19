class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr=0
        max_e=0
        for i in range(0,len(gain)):
            curr+=gain[i]
            max_e=max(curr,max_e)
        return max_e
        
