class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        mini = min(strs)
        
        maxi = max(strs)

        k=""

        for i in range(len(mini)):
            if(mini[i]==maxi[i]):
                k+=mini[i]

            else:
                break

        return k


        
                

                

        
