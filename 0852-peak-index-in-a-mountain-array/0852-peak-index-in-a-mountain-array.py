class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.find_peak(arr,0,len(arr))
            
    def find_peak(self, arr:List[int], start, end):
        if end - start == 1:
            return start
        
        if end - start == 2:
            if arr[start] > arr[end]:
                return start
            else:
                return end
        
        mid = (start+end) // 2
        
        left_diff = arr[mid] - arr[mid-1]
        right_diff = arr[mid+1] - arr[mid]
        
        grad = (left_diff * right_diff) > 0
        
        if not grad:
            return mid
        
        else:
            if arr[mid-1] > arr[mid+1]:
                return self.find_peak(arr,start,mid+1)
            else:
                return self.find_peak(arr,mid+1,end)
                

        
        