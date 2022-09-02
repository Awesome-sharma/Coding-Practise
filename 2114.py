# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

class Solution:
    def mostWordsFound(self, s: List[str]) -> int:
        c = 0
        for i in s:
            a = list(map(str,i.split(" ")))
            c = max(c,len(a))
        return c
