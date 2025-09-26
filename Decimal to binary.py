class Solution:
    def decToBinary(self, n):
        # The built-in function bin() in Python converts an integer
        # into a binary string representation.
        # Example: bin(10) --> '0b1010'
        
        # [2::] is used for slicing the string.
        # - The '0b' at the beginning of the string indicates binary format.
        # - By slicing from index 2 onward, we remove '0b' and keep only the digits.
        # Example: bin(10) = '0b1010' --> bin(10)[2::] = '1010'
        
        return bin(n)[2::]
