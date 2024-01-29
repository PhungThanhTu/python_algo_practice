# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        long_string,short_string = s2,s1 
        if len(s1) > len(s2):
            return False
        short_char_map = {}
        long_char_map = {}
        l_len = len(long_string)
        s_len = len(short_string)
        for char in short_string:
            short_char_map[char] = 1 + short_char_map.get(char, 0)

        # initialize long_char_map
        for char in long_string[0: s_len]:
            long_char_map[char] = 1 + long_char_map.get(char, 0)
        
        if long_char_map == short_char_map:
            return True
        
        # start comparing
        for left in range(1, l_len - s_len + 1):
            right = left + s_len - 1
            long_char_map[long_string[left-1]] -= 1
            if long_char_map[long_string[left-1]] == 0:
                del long_char_map[long_string[left-1]]
            long_char_map[long_string[right]] = 1 + long_char_map.get(long_string[right], 0)

            if long_char_map == short_char_map:
                return True
        return False



print(Solution().checkInclusion("ab", "a"))