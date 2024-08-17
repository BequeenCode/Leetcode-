class Solution:
    def interpret(self, command: str) -> str:
        result = command.replace("()", "o")
        result = result.replace("(al)", "al")
        return result
