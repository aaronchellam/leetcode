class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        # Convert integer into a list of digits.
        num_str = str(num)
        digits = [int(digit) for digit in num_str]
        roman_string = ""

        # Process the thousands.
        if len(digits) >= 4:
            thousands_digit = digits[0]
            roman_string += "M" * thousands_digit
            digits = digits[1:]

        # Process the hundreds.
        if len(digits) >= 3:
            hundreds_digit = digits[0]
            if hundreds_digit <= 3:
                roman_string += "C" * hundreds_digit
            elif hundreds_digit == 4:
                roman_string += "CD"
            elif 5 <= hundreds_digit <= 8:
                roman_string += "D"
                roman_string += "C" * (hundreds_digit - 5)
            else:
                roman_string += "CM"

            digits = digits[1:]

        # Process the tens.
        if len(digits) >= 2:
            tens_digit = digits[0]

            if tens_digit <= 3:
                roman_string += "X" * tens_digit
            elif tens_digit == 4:
                roman_string += "XL"
            elif 5 <= tens_digit <= 8:
                roman_string += "L"
                roman_string += "X" * (tens_digit - 5)
            else:
                roman_string += "XC"

            digits = digits[1:]

        # Process the ones.
        if len(digits) >= 1:
            roman_string += dict[digits[0]]

        return roman_string

    def intToRomanSimplified(self, num: int) -> str:
        roman_numerals = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1)
        ]

        result = ""

        for roman, value in roman_numerals:
            while num >= value:
                result += roman
                num -= value

        return result


if __name__ == '__main__':
    num = 1210
    sol = Solution().intToRoman(num)
    print(sol)
