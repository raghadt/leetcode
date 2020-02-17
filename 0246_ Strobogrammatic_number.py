class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic ={'6':'9', '8':'8', '9':'6', "1":"1", "0":"0"}
        return num[::-1] == "".join(dic[i] for i in num if i in dic.keys())