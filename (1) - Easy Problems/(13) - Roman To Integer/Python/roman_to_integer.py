class Solution:
    def __init__(self):
        self.numerals = {'I': 1,
                         'V': 5,
                         'IV': 4,
                         'IX': 9,
                         'X': 10,
                         'XL': 40,
                         'L': 50,
                         'XC': 90,
                         'C': 100,
                         'CD': 400,
                         'D': 500,
                         'CM': 900,
                         'M': 1000}

    def romanToInt(self, s: str) -> int:
        # Get a list of every character in the string
        chars = [char for char in s.upper()]
        result = 0
        i = 0

        while (i < len(chars)):
            # Check 2 chars at a time
            pair = ''.join(chars[i:i + 2])

            # If the pair is found in the dictionary
            # then we can skip 2 indices ahead.
            if pair in self.numerals:
                result += self.numerals.get(pair)
                i += 2
            else:  # If not we read 1 character only
                result += self.numerals.get(pair[0])
                i += 1

        return result


# Test cases
sol = Solution()
assert sol.romanToInt('III') == 3
assert sol.romanToInt('LVIII') == 58
assert sol.romanToInt('MCMXCIV') == 1994
