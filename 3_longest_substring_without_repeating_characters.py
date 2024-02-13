class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_dict = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_dict:
                # Slide start index to the right if there is a duplicate character in the window.
                # If the end pointer finds a character in the map, we must only change the start pointer if the map character index is within the sliding window.
                start = max(char_dict[s[end]] + 1, start)

            char_dict[s[end]] = end
            max_length = max(max_length, end - start + 1)


        return max_length


print(Solution().lengthOfLongestSubstring("abba"))