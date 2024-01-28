class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        maxCount = 0
        freq_map = {}
        if len(s) == 0 or len(s) == 1:
            return len(s)
        for end in range(len(s)):
            freq_map[s[end]] = 1 + freq_map.get(s[end], 0)
            max_val = max(freq_map.values())
            if len(s[start:end+1]) - max_val > k:
                freq_map[s[start]] -= 1
                start += 1
            print(s[start:end+1])
            print(freq_map)
            maxCount = max(len(s[start:end+1]), maxCount)
        return maxCount

print(Solution().characterReplacement("ABAA", 0))