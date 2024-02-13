def reverse(self, x: int) -> int:
    # Check if x is -ve
    is_negative = False
    if x < 0:
        is_negative = True
        x = abs(x)

    # Reverse the string by using a -1 step.
    reversed_str = str(x)[::-1]
    reversed_int = int(reversed_str)

    # Correct for negative.
    if is_negative:
        reversed_int *= -1

    # Check if reversed integer is within the 32-bit signed range.
    if reversed_int < -2**31 or reversed_int > 2**31 - 1:
        return 0

    return reversed_int