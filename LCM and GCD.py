import math
from typing import List

class Solution:
    def lcmAndGcd(self, a: int, b: int) -> List[int]:
        # Step 1: Calculate GCD using math.gcd()
        # gcd(a, b) = greatest number that divides both a and b
        gcd_val = math.gcd(a, b)

        # Step 2: Calculate LCM using the formula:
        # lcm(a, b) = (a * b) // gcd(a, b)
        # abs() ensures positivity even if numbers are negative
        lcm_val = abs(a * b) // gcd_val

        # Step 3: Return the result as a list [LCM, GCD]
        return [lcm_val, gcd_val]
