class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort alphabetical, create a map "abc" : ["cad", "dac"]
        # return map.items()
        if len(strs) == 1:
            return [strs]

        key2ana = defaultdict(list)
        for s in strs:
            sort_s = "".join(sorted(s))
            key2ana[sort_s].append(s)
        return list(key2ana.values())
