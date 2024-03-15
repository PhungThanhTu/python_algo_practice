from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key= lambda x:x[2])
        time_map = {}
        for p1, p2, t in meetings:
            time_map[t] = time_map.get(t, [])
            time_map[t].append([p1, p2])
        
        secrets = { 0, firstPerson}

        for key in time_map:
            meeting = time_map[key]
            seen = set()
            graph = {}
            for a, b in meeting:
                graph[a] = graph.get(a, [])
                graph[b] = graph.get(b, [])
                graph[a].append(b)
                graph[b].append(a)
                if a in secrets:
                    seen.add(a)
                if b in secrets:
                    seen.add(b)
            queue = list(seen)[::]
            while queue:
                node = queue.pop()
                for i in graph[node]:
                    if i not in secrets:
                        secrets.add(i)
                        queue.append(i)          
        return list(secrets)
    
print(Solution().findAllPeople(4 ,[[3,1,3],[1,2,2],[0,3,3]], 3))