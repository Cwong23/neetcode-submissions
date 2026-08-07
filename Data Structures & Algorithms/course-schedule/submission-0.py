class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for crs, prereq in prerequisites:
            graph[crs].append(prereq)
        visited, visiting = set(), set()
        
        def dfs(i):
            if i in visited:
                return True
            if i in visiting:
                return False
            
            visiting.add(i)

            for prereq in graph[i]:
                if not dfs(prereq):
                    return False
            visited.add(i)
            visiting.remove(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True