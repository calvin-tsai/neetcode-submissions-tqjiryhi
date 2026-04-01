class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #anagram = same letters, different order
        #sort the word
        s, t = sorted(s), sorted(t)
        return s == t