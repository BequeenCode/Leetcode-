class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol= [], ['(']

        def backtrack(openCount, closeCount):
            if openCount==n:
                for _ in range(closeCount, n):
                    sol.append(')')
                ans.append(''.join(sol[:]))
                for _ in range(closeCount, n):
                    sol.pop()
                return

            if closeCount> openCount:
                return 

            sol.append('(')
            backtrack(openCount+1, closeCount)
            sol.pop()

            sol.append(')')
            backtrack(openCount, closeCount+1)
            sol.pop()

        backtrack(1,0)
        return ans