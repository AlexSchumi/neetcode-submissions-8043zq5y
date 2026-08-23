class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return self.myPow(1 / x, -n)
            
        half = self.myPow(x, n // 2)
        
        return half * half if n % 2 == 0 else half * half * x
        