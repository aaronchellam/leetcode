# n can be negative
import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n == 1:
            return x

        if n > 0:
            first_pow = math.floor(n / 2)
            second_pow = math.ceil(n / 2)

            print(f"\nComputing {x}^{n}")
            print(f"First Power: {first_pow}")
            print(f"Second Power: {second_pow}")
            print(f"Computing {x}^{n} = {x}^{first_pow} * {x}^{second_pow}")

            first_term = self.myPow(x, first_pow)

            if first_pow == second_pow:
                return first_term * first_term
            else:
                return first_term * first_term * x


        else:
            return 1 / (self.myPow(x, -n))


if __name__ == '__main__':
    x = 0.00001
    n = 2147483648
    sol = Solution().myPow(x, n)
    print(sol)
