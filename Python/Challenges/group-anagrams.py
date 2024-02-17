class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res_list = []
        for i in range(0, len(strs)):
            for j in range(i, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    
        return res_list

    def isAnagram(self, s1: str, s2: str):
        if len(s1) == len(s2):
            if self.getWeight(s1) == self.getWeight(s2):
                if self.getMem(s1) == self.getMem(s2):
                    return True
        return False
    
    def getWeight(self, s: str):
        return sum([ord(c) for c in s])
    
    def getMem(self, s: str):
        mem = {}
        for c in s:
            if c not in mem:
                mem[c] = 1
            else:
                mem[c] += 1
        return mem


if __name__ == '__main__':
    res = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(res)