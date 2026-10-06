class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        dicts = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for _s in s:
            if _s in ['(', '[', '{']:
                stack.append(dicts[_s])
            else:
                if not stack:
                    return False
                right = stack.pop()
                if right != _s:
                    return False
        return len(stack) == 0

        