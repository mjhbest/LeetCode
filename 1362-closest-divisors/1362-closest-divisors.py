import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        plan_a = self.findDivisors(num+1)
        plan_b = self.findDivisors(num+2)
        
        d_a = plan_a[1] - plan_a[0]
        d_b = plan_b[1] - plan_b[0]
        
        if d_a <= d_b:
            return plan_a
        else:
            return plan_b
        return m
        
    def findDivisors(self, num):
        for div in range(int(math.sqrt(num))+1,1,-1):
            if num % div == 0:
                return [div,int(num/div)]
            
        return [1,num]
    
        