class Solution:
    def isValid(self, s: str) -> bool:
        dicts = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stacks = []
        for _s in s:
            if _s in list(dicts.keys()):
                stacks.append(dicts[_s])
            else:
                if not stacks:
                    return False
                para = stacks.pop(-1)
                if _s != para:
                    return False
        return True if not stacks else False

        