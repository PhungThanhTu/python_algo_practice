class TimeMap:

    def __init__(self):
        self.timeDictionary = {}
    def binarySearch(self, nums, target, start, end):
        pivot = int((start + end) / 2)
        if nums == [] or nums[0][1] > target:
            return -1
        if nums[-1][1] < target:
            return len(nums) - 1
        if pivot + 1 == len(nums) and nums[pivot][1] <= target:
            return pivot
        print(f'pivot {pivot} len {len(nums)}')
        print(f'pivot value {nums[pivot][1]} target {target}')
        if nums[pivot + 1][1] > target and nums[pivot][1] <= target:
            return pivot

        if target > nums[pivot][1]:
            return self.binarySearch(nums, target, pivot + 1, end)
        if target < nums[pivot][1]:
            return self.binarySearch(nums, target, start, pivot - 1)


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeDictionary:
            self.timeDictionary[key].append((value, timestamp))
            return
        self.timeDictionary[key] = [(value, timestamp)]
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeDictionary:
            return "o"
        array = self.timeDictionary[key]
        result = self.binarySearch(array, timestamp, 0, len(array) - 1)
        if result == -1:
            return "o"
        return array[result][0]


# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("assem","fat",20)
obj.set("assem","thin",40)
obj.set("hamza","thin",41)
print(obj.get("hamza",20))
