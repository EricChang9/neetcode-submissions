class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}

        for course in prerequisites:
            if course[0] in graph:
                graph[course[0]].append(course[1])
            else:
                graph[course[0]] = [course[1]]
        visited = set()
        curr_visiting = set()
        def search(v):
            nonlocal graph

            visited.add(v)
            curr_visiting.add(v)
            if v in graph:
                for u in graph[v]:
                    print(f"u:{u}, v:{v}")
                    if u in curr_visiting:
                        return False
                    if u not in visited:
                        if not search(u):
                            return False
            curr_visiting.remove(v)
            return True

        for u,v in graph.items():
            if u not in visited:
                cycle  = search(u)
                if not cycle:
                    return False

        return True
            

            