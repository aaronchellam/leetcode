class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a)-1, len(b)-1
        carry = 0
        result = []

        # Iterate through both strings from right to left.
        while i >= 0 or j >= 0 or carry:
            a_digit = 0
            b_digit = 0

            if i >= 0:
                a_digit = int(a[i])
            if j >= 0:
                b_digit = int(b[j])

            

            digit = a_digit + b_digit + carry
            carry = 0

            # If the digit sum is zero, prepend zero to the result.
            if digit == 0:
                result.insert(0, '0')
            elif digit == 1:
                result.insert(0, '1')
            elif digit == 2:
                result.insert(0, '0')
                carry = 1
            else:
                result.insert(0,'1')
                carry = 1

            i -= 1
            j -= 1
        return ''.join(result)


if __name__ == '__main__':
    sol = Solution()
    a = '11'
    b = '111101'
    print(sol.addBinary(a, b))
