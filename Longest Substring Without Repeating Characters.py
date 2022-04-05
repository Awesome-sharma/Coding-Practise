# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


import sys
class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        n = len(st)
        if n == 0:
            return 0
        else:
            windowStart = 0
            length = -sys.maxsize-1 
            # Store index of each character
            positionMap = {}
            
            for windowEnd in range(n):
                rightChar = st[windowEnd]
                if rightChar in positionMap:
                    windowStart = max(windowStart, positionMap[rightChar] + 1)
                positionMap[rightChar] = windowEnd
                length = max(length, windowEnd - windowStart + 1)
            return length
          
          
