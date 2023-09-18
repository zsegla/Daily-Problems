# https://leetcode.com/problems/counting-words-with-a-given-prefix/



# solution one 
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word[:len(pref)] == pref:
                count += 1
        return count 

# solution two
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if word.startswith(pref):
                count += 1
        return count 
