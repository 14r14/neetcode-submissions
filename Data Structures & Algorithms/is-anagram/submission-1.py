class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        combined_str = list(s) + list(t)
        for char in set(combined_str):
            if t.count(char) != s.count(char):
                return False
        return True