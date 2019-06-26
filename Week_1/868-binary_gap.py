class Solution:
    """
    The naive solution runs at O(n^2), but my solution runs at O(n). The trick is to save
    the '1's' indexes in a list, then every index in the list can be compared with their
    neighbor to obtain the difference.
    """
    def binaryGap(self, N: int) -> int:
        index_list = []
        
        i = N
        cnt = 0
        while i != 0:
            if i % 2 == 1:
                index_list.append(cnt)
            
            i //= 2
            cnt += 1
            
        if len(index_list) < 2:
            return 0
        
        largest_dist = 0
        for i in range(1, len(index_list)):
            diff = index_list[i] - index_list[i-1]
            
            if diff > largest_dist:
                largest_dist = diff
                
        return largest_dist
