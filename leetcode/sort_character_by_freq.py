class Solution:
    def heapify(self, arr, root, predicate):
        # intialize largest as root
        largest = root

        # get left and right child
        left = root * 2 + 1
        right = root * 2  + 2

        # if left larger than largest
        if left < len(arr) and predicate(arr[left], arr[largest]):
            largest = left
        # if right larget than largest
        if right < len(arr) and predicate(arr[right], arr[largest]):
            largest = right
        # if largest is not root
        if largest != root:
            # make it root
            arr[root], arr[largest] = arr[largest], arr[root]
            # heapify affected sub-tree
            self.heapify(arr, largest, predicate)
    def build_heap(self, arr, predicate):
        start_index = int((len(arr) / 2) - 1)
        for i in range(start_index, -1, -1):
            self.heapify(arr, i, predicate) 


    def frequencySort(self, s: str) -> str:
        freq_map = {}
        result = []
        for i in s:
            freq_map[i] = 1 + freq_map.get(i, 0)
        queue = list(freq_map.items())
        # define lambda predicate
        max_predicate = lambda a,b: a[1] >= b[1]

        # get start index (last non leaf node)
        start_index = int((len(queue)) / 2 ) - 1
        print(f'start index {start_index}')
        sorted_queue = []

        self.build_heap(queue, max_predicate)
        while queue:
            # swap first and last
            first = 0
            last = len(queue) - 1

            queue[first], queue[last] = queue[last], queue[first]
            # pop
            res = queue.pop()

            # get result
            sorted_queue.append(res)
            # heapify again
            self.build_heap(queue, max_predicate)


        for i in range(len(sorted_queue)):
            for _ in range(sorted_queue[i][1]):
                result.append(sorted_queue[i][0])
        return "".join(result)
            

print(Solution().frequencySort("abaccadeeefaafcc"))

# 5
# 3          4
#1 1        2