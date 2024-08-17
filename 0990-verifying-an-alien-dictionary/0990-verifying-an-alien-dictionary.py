
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_map = {char: index for index, char in enumerate(order)}
        
        translated_words = [[order_map[char] for char in word] for word in words]
        return all(translated_words[i] <= translated_words[i + 1] for i in range(len(words) - 1))

# Example usage:
solution = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(solution.isAlienSorted(words, order))  
