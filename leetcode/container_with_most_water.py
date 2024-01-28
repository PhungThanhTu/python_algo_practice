
# https://leetcode.com/problems/container-with-most-water/
def maxArea(height: List[int]) -> int:
    max_volume = 0
    p0 = 0
    p1 = len(height) - 1
    while True:
        w = p1 - p0
        h = min(height[p1], height[p0])
        volume = w * h
        if volume > max_volume:
            max_volume = volume
        if height[p1] > height[p0]:
            p0 += 1
        else:
            p1 -= 1
        if p1 == p0 or p1 < p0:
            break
    return max_volume

heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))