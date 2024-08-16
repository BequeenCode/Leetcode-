class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t

solution = Solution()
num = 4
t = 1
print(solution.theMaximumAchievableX(num, t))  
