class Solution:
    def myPow(self, x: float, n: int) -> float:
        val = 1
        cnt = n 
        
        if n < 0:
            cnt = n*-1
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n == -1:
            return 1/x
        
        
        if cnt%2 ==0:
            half = self.myPow(x,cnt//2)  
            val = half*half
        
        else:
            half = self.myPow(x,(cnt-1)//2)  
            val = half*half * x
            
            
        ## terminate
        if n < 0:
            return 1/val
    
        return val
    
    
            