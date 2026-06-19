class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=set(nums)
        n=len(nums)
        res=[]
        for i in range(1,n+1):
            if i not in l:
                res.append(i)
        return res
                    
