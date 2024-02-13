from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find the length of the smallest string. This is the maximum prefix size.
        min_length = min(len(s) for s in strs)

        max_prefix_size = 0

        for i in range(min_length, 0, -1):
            prefix = strs[0][:i]

            for s in strs:
                if s[:i] != prefix:
                    prefix = ''
                    break

            if len(prefix) != 0:
                return prefix

        return ''

if __name__ == '__main__':
    sol = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(sol)