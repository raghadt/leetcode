#---------- 5% lol

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        s_list.reverse()
        for i in t:
            if i in s_list:
                s_list.pop()

        return len(s_list)==0





#--------- #92% wow
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0

        for c in s:
            i = t.find(c, start) #don't look before start
            # print(i)
            if i == -1:
                return (False)
            start = i + 1
        return (True)