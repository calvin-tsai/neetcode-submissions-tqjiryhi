class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram = same letters, different order
        # if diff lengths, never going to be an anamgram
        if len(s) != len(t):
            return False
        #add everything to a hashmap
        s_counts = {}
        t_counts = {}
        for i in range(len(s)):
            s_counts[s[i]] = s_counts.get(s[i], 0) + 1
            t_counts[t[i]] = t_counts.get(t[i], 0) + 1
        return s_counts == t_counts