# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31 -1
# n is an integer.
# Either x is not zero or n > 0.
# -104 <= xn <= 104

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
     
