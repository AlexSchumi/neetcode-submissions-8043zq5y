class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur_str, left_cnt, right_cnt):
            # stop criteria
            if right_cnt == n and len(cur_str)==n*2:
                res.append(cur_str)
            if left_cnt > n:
                return

            # loop to generate parentheses
            if left_cnt > right_cnt:
                dfs(cur_str+')', left_cnt, right_cnt+1)
                dfs(cur_str+'(', left_cnt+1, right_cnt)
            elif left_cnt == right_cnt:
                dfs(cur_str+'(', left_cnt+1, right_cnt)
            else:
                return
        dfs('', 0, 0)
        return res
            
            

            




        