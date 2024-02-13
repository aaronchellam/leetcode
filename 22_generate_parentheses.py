from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate_helper(n, n, "", result)
        return result

    def generate_helper(self, left, right, current_str, result):
        # Base case: both left and right parentheses are used up.
        if left == 0 and right == 0:
            result.append(current_str)
            return


        # Recursive cases.
        if left > 0:
            self.generate_helper(left-1, right, current_str + "(", result)
        if right > left:
            self.generate_helper(left, right - 1, current_str + ")", result)







        # stack = []
        #
        # # At certain points, we can either add an open or closed bracket.
        # # There can only by n open brackets.
        # options = ['(', ')']
        #
        # result = []
        #
        # def backtrack(combination, open_count, closed_count):
        #     if open_count == n:
        #         remaining_closed = open_count - closed_count
        #         for i in range(remaining_closed):
        #             combination.append(')')
        #
        #         result.append(''.join(combination))
        #         return
        #
        #     for option in options:
        #         combination.append(option)
        #         if option == '(':
        #             open_count += 1
        #         else:
        #             closed_count += 1
        #         backtrack(combination, open_count, closed_count)
        #         combination.pop()
        #         if option == ')':
        #             closed_count -= 1
        # backtrack([], 0, 0)
        # return result


if __name__ == '__main__':
    sol = Solution().generateParenthesis(n=3)
    print(sol)
