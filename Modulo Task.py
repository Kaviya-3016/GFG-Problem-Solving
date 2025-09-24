# User function Template for python3

class Solution:
    def modTask(self, N):
        # code here
        # N = int(input())  # (Not needed here, because N is already given as input in test cases)

        # Loop from 1 to N-1
        for i in range(1, N):
            # Calculate remainder when N is divided by i
            large = N % i

            # If remainder is at least 1, return (N//2 + 1)
            # Why? Because mathematically, the maximum remainder of N % i
            # always occurs when i = (N//2) + 1
            return (N // 2) + 1

        # Special case: if N == 1, no loop runs
        # So we handle it separately and return 1
        if N == 1:
            return 1
