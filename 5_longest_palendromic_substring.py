class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_len = 0
        best_l = 0
        best_r = 0

        for i in range(len(s)):
            # odd length
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > longest_len:
                    longest_len = r-l+1
                    best_l = l
                    best_r = r

                l -= 1
                r += 1

            # even length
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l + 1) > longest_len:
                    longest_len = r-l+1
                    best_l = l
                    best_r = r

                l -= 1
                r += 1

        return s[best_l:best_r+1]

print(Solution().longestPalindrome("babad"))