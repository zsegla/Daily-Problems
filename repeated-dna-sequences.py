# https://leetcode.com/problems/repeated-dna-sequences/



class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subs, rep = set(), set()
        target  = 10

        for i in range(len(s)-target+1):
            sub = s[i:i+target]
            if sub in subs:
                rep.add(sub)
            else:
                subs.add(sub)

        return list(rep)
