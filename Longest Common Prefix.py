# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(self, s: List[str]) -> str: 
    check = min(s)
    k = m = ""
    for i in range(len(check)):
        c = 0
        for j in range(len(s)):
            if check[i] == s[j][i]:
                c+=1
                m = s[j][i]
        if c == len(s):
            k += m
        else:
            break
    return k
