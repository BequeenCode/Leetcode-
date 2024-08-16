
class Solution:
    def average(self, salary: List[int]) -> float:

        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary) / len(salary)

# Example usage:
solution = Solution()
salary = [4000, 3000, 1000, 2000]
print(f"{solution.average(salary):.5f}")  
