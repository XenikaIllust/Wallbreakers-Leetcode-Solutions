class Solution:
    
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        '''
        My first solution only accounted for square matrices, but it was a little more memory efficient. If m
        is the no. of rows, and n is the no. of cols: The time complexity is O(mxn). The space complexity is 
        O(mxn).
        '''
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j or j < i:
                    pass
                else:
                    temp = A[i][j]
                    A[i][j] = A[j][i]
                    A[j][i] = temp
        
        '''
        My second solution did something smarter, by initializing an empty matrix before copying the elements
        with flipped indices. This solves the problem of non-square matrices. However it consumes more memory.
        The time complexity is O(mxn). The space complexity is O(mxn).
        '''
        
        row_num = len(A)
        col_num = len(A[0])
        
        res = [[0] * row_num for x in range(col_num)]
        
        for i in range(row_num):
            for j in range(col_num):
                res[j][i] = A[i][j]
                
        return res
