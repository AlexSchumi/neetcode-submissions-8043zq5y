class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i, j, cur_word, visit):
            if cur_word == word:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in visit:
                return False

            visit.add((i, j))
            res = dfs(i+1, j, cur_word+board[i][j], visit) or \
                  dfs(i-1, j, cur_word+board[i][j], visit) or \
                  dfs(i, j+1, cur_word+board[i][j], visit) or \
                  dfs(i, j-1, cur_word+board[i][j], visit)
            visit.remove((i, j))
        
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visit = set()
                    res = dfs(i, j, '', visit)
                    if res:
                        return True
        return False

        