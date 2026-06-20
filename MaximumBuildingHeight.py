class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort()
    
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + (restrictions[i][0] - restrictions[i - 1][0]))
        
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + (restrictions[i + 1][0] - restrictions[i][0]))
        
        max_height = 0
        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
        
        return max_height


        
     
    
