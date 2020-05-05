class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #row and columns of the empty position
        find = self.find_empty(board)
        if not find:
            return True
        else:
             row,column=self.find_empty(board)
        for i in range(1,10):
            if self.valid_number(board,i,(row,column)):
                board[row][column]=str(i)
                
                if self.solveSudoku(board):
                    return True
                else:
                    board[row][column]='.'
        return False
    
    
    
    def find_empty(self,bo: List[List[str]]):
        for i in range(len(bo)):
            for j in range(len(bo)):
                if bo[i][j]==  '.':
                    return i,j #row and column of the empty position
        return None
    
    

        return True
    def valid_number(self,bo,num,pos):
        
        #check row
        for j in range(len(bo)):
            if bo[pos[0]][j]==str(num) and pos[1]!=j:
                return False
        
        #check column
        for i in range(len(bo)):            
            if bo[i][pos[1]]==str(num) and pos[0]!=i:
                return False
            
        #check 3x3 sub-boxes
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
    
                if bo[i][j]==str(num) and (i,j)!=pos:
                    return False
        return True
                
        
