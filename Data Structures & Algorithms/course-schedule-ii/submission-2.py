class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use a dfs approach through the entire graph
        # use a visit set - if we have already seen along the path, return []
        # use a hashmap - course to prereq
        # continue until we hit a [], as we backtrack, remove from the visit set

        
        m = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites: # add to the hashmap
            m[crs].append(pre)
        res = []
        visit, cycle = set(), set()

        # O(V + E) T
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for p in m[crs]: #for each prerequisite in the course
                if not dfs(p):
                    return False

            cycle.remove(crs) # remove the course after we backtrack back to current course
            visit.add(crs)
            res.append(crs)
            return True
    
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res