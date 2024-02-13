class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Create a string for each row.
        rows = ['' for _ in range(numRows)]

        down = True
        row = 0

        for char in s:
            rows[row] += char

            if down:
                row += 1

            else:
                row -= 1

            if row == numRows - 1:
                down = False

            elif row == 0:
                down = True

        return ''.join(rows)


print(Solution().convert("PAYPALISHIRING", 3))
