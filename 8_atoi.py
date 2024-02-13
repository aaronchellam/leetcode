class Solution:
    def myAtoi(self, s: str) -> int:
        # Strip leading whitespace.
        s = s.lstrip()

        # Parse the sign.
        sign = 1
        if s and (s[0]=='-' or s[0]=='+'):
            if s[0]=='-':
                sign = -1

            s = s[1:]

        # Read in the digits.
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)

        # Apply the sign.
        num *= sign

        # Clamp within 32-bit signed integer range.
        return max(min(num, 2**31 - 1), -2**31)
