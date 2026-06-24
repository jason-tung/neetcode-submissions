class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = []
        words = [word1, word2]
        m = max(len(word) for word in words)
        for i in range(m):
            for letter_i in range(len(words)):
                if i < len(words[letter_i]):
                    l.append(words[letter_i][i])
        return ''.join(l)
