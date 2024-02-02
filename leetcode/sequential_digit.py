# https://leetcode.com/problems/sequential-digits/
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = "123456789"

        num_digit_low = len(str(low))
        num_digit_high = len(str(high))
        result = []
        for num_digits in range(num_digit_low, num_digit_high + 1):
            left = 0
            for left in range(0, 10 - num_digits):
                right = left + num_digits - 1
                num = int(nums[left:right+1])
                if low <= num <= high:
                    print(num)
                    result.append(num)
        return result

print(Solution().sequentialDigits(1000, 13000))