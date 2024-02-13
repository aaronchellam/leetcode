from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            t = t.replace(char, '', 1)

        return len(t) == 0

    # Don't continuously replace the string with a new string.
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        # Default dictionary with int values.
        s_counter, t_counter = defaultdict(int), defaultdict(int)
        for s_char, t_char in zip(s, t):
            s_counter[s_char] += 1
            t_counter[t_char] += 1

        return s_counter == t_counter


