# https://leetcode.com/problems/valid-sudoku/


board =     [["5","3",".",".","7",".",".",".","."]
,["6","3",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def flatten(board):
    flattened_board = []
    for i in range(9):
        row_index = int(i % 3) * 3
        column_index = int(i / 3) * 3
        mini_board = []
        for k in range(3):
            for l in range(3):
                mini_board.append(board[k + column_index][l + row_index])
        flattened_board.append(mini_board)
    return flattened_board


def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # columns
        for i in range (9):
            presence_dic = {}
            for k in range (9):
                p = board[k][i]
                print(presence_dic)
                if p != ".":
                    if p in presence_dic:
                        return "false"
                    presence_dic[p] = True
        # rows
        for i in range (9):
            presence_dic = {}
            for k in range (9):
                p = board[i][k]
                print(presence_dic)
                if p != ".":
                    if p in presence_dic:
                        return "false"
                    presence_dic[p] = True
        # nine 3x3 box
        ## flatten 3x3 box
        flattened_board = flatten(board)
        for i in range (9):
            presence_dic = {}
            for k in range (9):
                p = flattened_board[i][k]
                print(presence_dic)
                if p != ".":
                    if p in presence_dic:
                        return "false"
                    presence_dic[p] = True
                    
        return "true"

                
print(isValidSudoku(board))


