class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # try:
        #     # String.index(sub) method returns the lowest index where substring sub is found in the String.
        #     index = haystack.index(needle)
        #     return index
        # except ValueError:
        #     return -1

        # LPS: What is the longest proper prefix that is also a suffix?
        # The LPS array gives the length of the LPS for each prefix of the needle.
        # Initialise LPS array.
        lps = [0] * len(needle)

        # Create variable pre to figure out the lps for each prefix in the needle.
        pre = 0

        # Iterate across the needle to fill in the lps array. First value is always zero so start from index 1.
        for i in range(1, len(needle)):

            # If the pre and i pointers do not have matching chars, move the pre pointer back to its appropriate place.
            # This appropriate place is determined by the lps value at the pre-1 index as this contains the length of
            # lps of the prefix already scanned by the pre pointer before the mismatch.
            while (pre > 0 and needle[i] != needle[pre]):
                pre = lps[pre-1]

            # If the pre pointer and i pointer have matching chars, advance the pre pointer up by 1. Then assign the lps
            # value at index i to be the index of the pre pointer.
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre


        # MAIN ALG

        # Needle index.
        n = 0

        # Iterate through haystack.
        for h in range(len(haystack)):

            # Move n back whenever there is a mismatch in the needle and the haystack.
            while (n > 0 and needle[n] != haystack[h]):
                # Of the section of the needle that did match, what was the length of the lps?
                n = lps[n-1]

            # Increment n if there is a match.
            if needle[n] == haystack[h]:
                n += 1


            if n == len(needle):
                return h - n + 1

        return -1
