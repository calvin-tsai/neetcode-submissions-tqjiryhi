class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        letter_counts = {}
        res = 0
        for r in range(len(s)):
            letter_counts[s[r]] = letter_counts.get(s[r], 0) + 1
            while (r - l + 1) - max(letter_counts.values()) > k:
                letter_counts[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res