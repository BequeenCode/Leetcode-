class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their corresponding integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current value is less than the next value, subtract it
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            # Otherwise, add it
            else:
                total += roman_to_int[s[i]]
        
        return total
