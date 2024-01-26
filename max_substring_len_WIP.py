class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStringChar = []
        for i in range(len(s)):
            if subStringChar and s[i] == subStringChar[0]:
                print(f's[{i}]: {s[i]} substringchar {subStringChar[0]}')
                subStringChar.pop(0)
            if subStringChar and s[i] == subStringChar[-1]:
                subStringChar.pop()
            subStringChar.append(s[i])    
            print(subStringChar)
        return len(subStringChar)
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))