class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        orders = []
        
        for k in range(len(arr),1,-1):
            bigIndex = arr.index(max(arr[:k]))
            if bigIndex+1 != k:
                arr[0:bigIndex+1] = arr[0:bigIndex+1][::-1]
                orders.append(bigIndex+1)

                arr[0:k] = arr[0:k][::-1]
                orders.append(k)
        return orders




        