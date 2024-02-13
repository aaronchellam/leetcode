class Solution:
    # Binary search edition.
    def mySqrt2(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            next_square = (mid+1) * (mid+1)


            if square <= x and x < next_square:
                return mid

            if square < x:
                left = mid + 1
            # x < square
            else:
                right = mid-1





    def mySqrt(self, x: int) -> int:
        root = 0
        while True:
            square = root * root

            if square > x:
                break

            root += 1

        return root - 1
