class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        if not s:
            return 0

        i, sign, num = 0, 1, 0
        n = len(s)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        if s[i] in "+-":
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])

            if num * sign > INT_MAX:
                return INT_MAX
            if num * sign < INT_MIN:
                return INT_MIN

            i += 1

        return num * sign