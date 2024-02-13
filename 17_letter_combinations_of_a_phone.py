from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters.
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(combination, index):
            # Base case: If the combination is complete, add it to the result
            if index == len(digits):
                result.append(''.join(combination))
                return

            # Get the letters corresponding to the current digit
            current_letters = digits_to_letters[digits[index]]

            # Iterate over the letters and make recursive calls
            for letter in current_letters:
                combination.append(letter)
                backtrack(combination, index + 1)
                combination.pop()  # Backtrack by removing the last letter

        backtrack([], 0)
        return result


if __name__ == '__main__':
    digits = "773956362"
    sol = Solution().letterCombinations(digits)
    print(sol)
    print(len(sol))
