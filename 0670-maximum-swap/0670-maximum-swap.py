class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = self.switchMax(str(num))
            
        return int(arr)
    
    def switchMax(self,num,start_index=0):
        if start_index == len(num)-1:
            return num
        
        if max(num[start_index:]) == num[start_index]:
            return self.switchMax(num,start_index+1)
        
        else:
            start_digit = num[start_index]
            max_index = num[start_index:].rfind(max(num[start_index:])) + start_index
            max_digit = num[max_index]
            
            arr = list(num)
            arr[start_index] = max_digit
            arr[max_index] = start_digit
            return "".join(arr)
            
    
    