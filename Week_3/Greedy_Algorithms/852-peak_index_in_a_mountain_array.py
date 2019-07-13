"""
My approach is to conduct binary search on the array itself rather than create nodes and link them.
"""

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def recursiveBinaryPeakSearch(A, start, end, target_ind):
            if start == end:
                return
            
            mid = (end-start) // 2 + start
            
            if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
                target_ind[0] = mid
                return
            
            recursiveBinaryPeakSearch(A, start, mid, target_ind)
            recursiveBinaryPeakSearch(A, mid+1, end, target_ind)
            
        target_ind = [None]
        recursiveBinaryPeakSearch(A, 1, len(A)-1, target_ind)
        
        return target_ind[0]
