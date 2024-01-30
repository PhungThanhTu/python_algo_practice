#https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def checkFreqmap(self, long_freqmap: dict, short_freqmap:dict) -> bool:
        for key in short_freqmap:
            if long_freqmap.get(key, 0) < short_freqmap[key]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        short_freqmap = {}
        long_freqmap = {}
        if len(t) > len(s):
            return ""
        # initialize freqmap of t
        for char in t:
            short_freqmap[char] = 1 + short_freqmap.get(char, 0)
        # initialize pointer
        left = 0
        right = 0
        shortest_substring = ""
        shortest_substring_len = float('inf')
        for right in range(len(s)):
            char = s[right]
            if char in short_freqmap:
                long_freqmap[char] = 1 + long_freqmap.get(char, 0)
                if self.checkFreqmap(long_freqmap, short_freqmap):
                    print(f'found valid {s[left:right+1]}')
                    # update min
                    if len(s[left:right+1]) < shortest_substring_len:
                        shortest_substring = s[left:right+1]
                        shortest_substring_len = len(s[left:right+1])

                    while (s[left] not in short_freqmap) or (s[left] in short_freqmap and long_freqmap[s[left]] > short_freqmap[s[left]]):
                        if s[left] in short_freqmap:
                            long_freqmap[s[left]] -= 1
                        left += 1
                        if len(s[left:right+1]) < shortest_substring_len:
                            shortest_substring = s[left:right+1]
                            shortest_substring_len = len(s[left:right+1])
        return shortest_substring
        


        

print(Solution().minWindow("ADOBECODEBANC", "ABC"))