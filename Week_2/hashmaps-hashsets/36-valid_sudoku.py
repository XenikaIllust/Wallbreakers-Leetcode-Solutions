"""
This implementation does not work for the edge case where the whole grid is empty. However, it solves valid sudoku!
TODO: revise solution
"""

from collections import defaultdict, Counter

BOARD_WIDTH = 9
BOARD_HEIGHT = 9

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def intersection(row_counts, col_counts, subgrid_counts):
            intersections = Counter()
            
            for key in row_counts:
                if col_counts[key] != 0 and subgrid_counts[key] != 0:
                    intersections.update({key: 1})
                    
            return intersections
        
        digits = [1,2,3,4,5,6,7,8,9]
        
        #find row possibilities for every square
        row_unused = defaultdict(list)
        
        for i, row in enumerate(board):
            digits_counter = Counter(digits)
            for j, square in enumerate(board[i]):
                if square != ".":
                    del digits_counter[int(square)]
                
            row_unused[i] = digits_counter
            
        #find col possibilities for every square
        col_unused = defaultdict(list)
        
        for i in range(BOARD_WIDTH):
            digits_counter = Counter(digits)
            for j in range(BOARD_HEIGHT):
                if board[j][i] != ".":
                    del digits_counter[int(board[j][i])]
                
            col_unused[i] = digits_counter
        
        #find 3x3 possibilities for every square
        subgrid_unused = defaultdict(list)
        
        count = 0
        for i in range(0, BOARD_WIDTH, 3):
            for j in range(0, BOARD_HEIGHT, 3):
                digits_counter = Counter(digits)
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        if board[a][b] != ".":
                            del digits_counter[int(board[a][b])]
                            
                subgrid_unused[count] = digits_counter
                count += 1
        
        # find intersections
        square_unused = defaultdict(lambda : defaultdict(lambda : {}))
        count = 0
        for i in range(0, BOARD_WIDTH, 3):
            for j in range(0, BOARD_HEIGHT, 3):
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        if board[a][b] == '.':
                            square_unused[a][b] = intersection(row_unused[a], col_unused[b], subgrid_unused[count])
                            
                count += 1
                
        # perform eliminations. 9 rounds because the maximum number of unused possibilities is 9 for each square
        
        for k in range(9):
            square_unused_copy = square_unused.copy()
            
            for row_key in square_unused_copy:
                for col_key in square_unused_copy[row_key]:
                    if len(square_unused_copy[row_key][col_key]) == 1:  
                        target = list(square_unused_copy[row_key][col_key].keys())[0]
                        target_row = row_key
                        target_col = col_key
                        del square_unused_copy[row_key][col_key][target]
                        board[target_row][target_col] = str(target)
                        
                        for p in square_unused_copy.keys():
                            for q in square_unused_copy[p].keys():
                                #elimination by row and column
                                if (p == target_row and q != target_col) or (p != target_row and q == target_col):
                                    del square_unused_copy[p][q][target]
                                    
                                #elimination by subgrid
                                if p in range(target_row - (target_row % 3), target_row + 3 - (target_row % 3)) \
                                and q in range(target_col - (target_col % 3), target_col + 3 - (target_col % 3)):
                                    del square_unused_copy[p][q][target]

            square_unused = square_unused_copy
        
        for i in range(BOARD_WIDTH):
            for j in range(BOARD_HEIGHT):
                if board[i][j] == '.' and len(square_unused[i][j]) > 0:
                    print(square_unused[i][j])
                    return False
                
        return True
