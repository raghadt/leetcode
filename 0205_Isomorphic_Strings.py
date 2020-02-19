#-------------- 39%

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_index = [s.find(i) for i in s]
        t_index = [t.find(i) for i in t]
        return s_index == t_index



# ---------- 78

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}

        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
                else:
                    dic[s[i]]=t[i]
        return True        