class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        array = nums1 + nums2
        array = self.mergeSort(array)

        total_len = len(nums1) + len(nums2)
        mid = total_len // 2

        if total_len %2 ==0:
            return (array[mid] + array[mid-1])/2
        else:
            return array[mid]
        return array[mid]
    
    def mergeSort(self, array):
        if len(array) ==1:
            return array

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        self.mergeSort(L)
        self.mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

        return array