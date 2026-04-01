class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # able to move along children
        
        preMap = {i : [] for i in range(numCourses)} # each number in range, add as a key and add an empty list

        for crs, pre in prerequisites: #get each value of prereqs
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet: #base case: course visited already, means loop
                return False
            if preMap[crs] == []: #has no prereqs, so its takeable and all courses along that are takeable
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]: # for each prereq for that course
                if not dfs(pre): return False #check if there's a loop, if not keep going

            # after the recursion, this means that there were no loops
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True



