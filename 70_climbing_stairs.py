class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialise the first two steps of the Fibonacci sequence.
        first, second = 1, 2

        # Calculate the number of wayys to climb for each step up to n.
        for i in range(3, n+1):
            current_step = first + second
            first = second
            second = current_step

        return second

if __name__ == '__main__':
    sol = Solution().climbStairs(8)
    print(sol)