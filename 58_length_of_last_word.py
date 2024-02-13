class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))