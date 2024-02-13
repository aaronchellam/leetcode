class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If char is closing bracket.
            if char in mapping:
                # Pop top element if stack is not empty, otherwise assign a dummy value.
                top = stack.pop() if stack else '#'

                if mapping[char] != top:
                    return False

            # If char is opening bracket, push onto stack.
            else:
                stack.append(char)

        # If the stack is not empty at the end, all open brackets have been closed in the correct order.
        return not stack


if __name__ == '__main__':
    sol = Solution()
    sol.isValid("{[]}")
    sol.isValid("([)]")

"""
Lessons:
- The stack data structure is essential for this.
"""