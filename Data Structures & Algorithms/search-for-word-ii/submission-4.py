class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not words:
            return []

        def word_search(i, j, word_idx, word):
            if word_idx >= len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[word_idx]:
                return False

            tmp = board[i][j]
            board[i][j] = '#'
            find = word_search(i + 1, j, word_idx + 1, word) or word_search(i - 1, j, word_idx + 1, word) or \
                   word_search(i, j - 1, word_idx + 1, word) or word_search(i, j + 1, word_idx + 1, word)
            board[i][j] = tmp
            return find

        results = []
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        res = word_search(i, j, 0, word)
                        if res:
                            results.append(word)
        return results
            

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()


        def dfs(r, c, node, word):
            #if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] not in node.children:
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] == '#' or board[r][c] not in node.children:
                return

            #visit.add((r, c))
            
            #tmp = board[r][c]
            #board[r][c] = '#'
            node = node.children[board[r][c]]
            word += board[r][c]
            tmp = board[r][c]
            board[r][c] = '#'
            if node.isWord:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            #visit.remove((r, c))
            board[r][c] = tmp
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)



           