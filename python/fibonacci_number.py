class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        one, two = 0, 1
        for _ in range(2, n + 1):
            one, two = two, one + two
        return two
#Time Complexity - O(n)
#Space Complexity - O(1)
