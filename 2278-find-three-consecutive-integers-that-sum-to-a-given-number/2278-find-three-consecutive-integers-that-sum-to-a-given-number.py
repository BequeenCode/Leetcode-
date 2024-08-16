class Solution:
    def sumOfThree(self, num: int) -> list[int]:
        quotient, remainder = divmod(num, 3)
        if remainder == 0:
            return [quotient -1, quotient, quotient + 1]
        return []   