from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate through all digits, starting from the rightmost.
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the digit is less than 9, add one and return the update array.
                digits[i] += 1
                return digits

            # If the digit is 9, set it to 0 and continue to the next left digit.
            else:
                digits[i] = 0

        # If all digits were 9, then append a 1 to the start of the array.
        return [1] + digits



if __name__ == '__main__':
    sol = Solution()
    digits = [9,9,9]
    print(sol.plusOne(digits))