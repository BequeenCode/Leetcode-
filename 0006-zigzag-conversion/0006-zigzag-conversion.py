class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        r=['']*numRows
        c=0
        g=False
        for i in s:
            r[c]+=i
            if c==0 or c==numRows-1:
                g=not g
            c+=1 if g else -1
        return ''.join(r)     