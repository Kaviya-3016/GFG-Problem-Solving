class Solution:
    def lastDigit(self, n: int) -> int:
        # Take the absolute value of n to handle negative numbers.
        # Example: if n = -123, abs(n) = 123
        # This ensures the last digit is always positive.
        last_digit = abs(n) % 10  

        # The modulo operator (%) gives the remainder when divided by 10.
        # For any integer, remainder of division by 10 is its last digit.
        # Example: 123 % 10 = 3

        # Return the extracted last digit
        return last_digit
