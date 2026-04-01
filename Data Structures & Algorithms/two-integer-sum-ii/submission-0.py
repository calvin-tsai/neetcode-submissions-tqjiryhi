class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # store numbers in a hash map - key is the value and val is the index
        # search through the array - if a key exists  that is target - num[i], return m[that value] and i

        m = {}
        res = []
        for i in range(len(numbers)):
            curr = numbers[i]
            if target - curr in m:
                res.append(m[target - curr] + 1)
                res.append(i + 1)
                return res
            m[curr] = i #add to the map
        return [-1]