class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0:
            return False
        elif n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        else:
            return False

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

if __name__ == '__main__':
    for i in range(17):
        sol = Solution().isPowerOfTwo(i)
        print(i)
        print(sol, "\n")

    # sol = Solution().isPowerOfTwo(4)