class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through entire list, alphabetize the string (so anagrams become the same)
        # use a hashmap where key is the alphabetized string and value are all the strings that match
        # return map.values()
        m = {}
        #O(m) time to loop through all values
        for s in strs:
            sAlpha = ''.join(sorted(s)) #O(nlogn)
            if sAlpha not in m:
                m[sAlpha] = []
            m[sAlpha].append(s)
        return m.values()
        # total time complexity: O(m * nlogn)