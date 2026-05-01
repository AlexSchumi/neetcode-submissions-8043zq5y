class Solution:
    # use python reverse
    # runtime complexity: O(N)
    # space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
        return cleaned_text == cleaned_text[::-1]
        
class Solution:
    # use python reverse
    # runtime complexity: O(N)
    # space complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char.lower() for char in s if char.isalnum())
    
        l, r = 0, len(cleaned_text)-1
        while l <= r and l >= 0 and l < len(cleaned_text):
            if cleaned_text[l] == cleaned_text[r]:
                l += 1
                r -= 1
            else:
                return False
        return True