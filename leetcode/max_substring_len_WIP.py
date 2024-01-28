class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        seen = {}
        max_len = 0
        for i in range(len(s)):
            end = i
            if s[i] in seen and seen[s[i]] > start:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            print(seen)
            max_len = max(max_len, len(s[start:end+1]))
            print(s[start:end+1])
        return max_len
            
print(Solution().lengthOfLongestSubstring("abba"))