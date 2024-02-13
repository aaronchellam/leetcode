class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map roman symbols to their corresponding values.
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialise the results variable.
        result = 0

        # Iterate through the Roman numeral string from right to left.
        for i in range(len(s)-1, -1, -1):
            # If the current symbol represents a smaller number than the next symbol, subtract its value.
            if i < len(s)-1 and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
                result -= roman_numerals[s[i]]
            else:
                result += roman_numerals[s[i]]

        return result

