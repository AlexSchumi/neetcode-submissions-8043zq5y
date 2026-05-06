class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(k, i, j, visit):      
            if k == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visit or board[i][j] != word[k]:
                return False

            visit.add((i,j))
            res =  dfs(k+1, i+1,j, visit) or dfs(k+1, i-1,j, visit) or \
                   dfs(k+1, i, j+1, visit) or dfs(k+1, i, j-1, visit)
            visit.remove((i,j))
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                visit = set()
                if board[i][j] == word[0]:
                    res = dfs(0, i, j, visit)
                    if res:
                        return True
        return False




        