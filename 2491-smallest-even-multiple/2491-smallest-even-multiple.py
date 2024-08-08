class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x=2*n
        i=2
        while (i%n!=0 and i%x!=0):
            i+=2
        return i
        