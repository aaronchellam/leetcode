def numberOfSteps(num: int) -> int:
    steps = 0
    while num != 0:
        steps += 1
        if (num % 2 == 0):
            num /= 2
        else:
            num -= 1

    return steps

def numberOfSteps2(num: int) -> int:
    # Get number in bit string form.
    digits = f'{num:b}'

    # Count every '0' once (division by 2).
    # Count every '1' twice (subtract 1 and then divide by 2).
    # Subtract 1 from the final solution as the leftmost '1' only requires one step.
    return digits.count('1') -1 + len(digits)


def recursiveNumberOfSteps(num: int, steps: int = 0) -> int:
    # num & 1 returns 0 if num is even.
    # num & 1 returns 1 if num is odds.
    # num >> 1 returns num/2 if num is even.
    return recursiveNumberOfSteps(num - 1 if num & 1 else num >> 1, steps + 1) if num else steps


print(numberOfSteps2(14))
