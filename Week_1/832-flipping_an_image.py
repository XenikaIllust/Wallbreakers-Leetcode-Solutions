class Solution:
    """
    I prefer not to traverse over the image twice as it results in O(n^2) time complexity and is inefficient. My solution transforms the image in place, so the space complexity is O(n).
    """
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def invert(a):
            if a == 0:
                return 1
            else:
                return 0
        
        row_num = len(A)
        col_num = len(A[0])
        
        for i in range(col_num):
            for j in range(row_num):
                if i < col_num // 2:
                    temp = A[j][i]
                    A[j][i] = invert(A[j][col_num - 1 - i])
                    A[j][col_num - 1 - i] = temp
                else:
                    A[j][i] = invert(A[j][i])
                
        return A
