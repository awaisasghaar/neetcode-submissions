# Brute Force approach

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         for i in range(len(s)):
#             for j in range(1 + 1, len(t)):
#                 if s[i] == t[j] or t[j] == s[i]:
#                     return True
#         return False

# Hash Map
# class Solution:
#     def isAnagram(self, s: str, t:str) -> bool:
        
#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)

#         return countS == countT

# Hash Table(Array)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord("r")] += 1
            count[ord(t[i]) - ord("r")] -= 1

        for value in count:
            if value != 0:
                return False
        return True

# Time Complexity: O(n)
# Space Complexity: O(1)






        