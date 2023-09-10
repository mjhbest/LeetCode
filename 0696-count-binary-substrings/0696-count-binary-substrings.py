from collections import deque

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        idx = 0
        cntList = []
        
        sames = deque()
        sames.append(s[0])
        
        while idx < len(s):
            idx += 1
            if idx == len(s):
                cntList.append(len(sames))
            
            elif sames[0] != s[idx]:
                cntList.append(len(sames))
                sames.clear()
                sames.append(s[idx])
            
            else:
                sames.append(s[idx])
    
        
        print(cntList)
        return sum([min(p) for p in pairwise(cntList)])
            
                