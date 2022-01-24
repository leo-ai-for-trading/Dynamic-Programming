class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        for i in range(len(word)):
            if word[0].isupper() and word[1:].islower():
                return True
            elif word.isupper():
                return True
            elif word.islower():
                return True
            else:
                return False
