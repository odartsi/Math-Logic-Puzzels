class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        for i in range(len(s)):
            if i > 0 and sym_val[s[i]] > sym_val[s[i - 1]]:
                number += sym_val[s[i]] - 2 * sym_val[s[i - 1]]
            else:
                number += sym_val[s[i]]
        return number
