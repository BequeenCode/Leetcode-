class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n%3==2:
            return False
        if n==1:
            return True
        return self.checkPowersOfThree(n//3)

        

        