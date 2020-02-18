class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


        vowls=[]
        for i in s[::-1]:
            if i in dic:
                vowls.append(i)
        st = ""
        ind=0
        for i in range(len(s)):
            if s[i] in dic:
                st+=vowls[ind]
                ind+=1
            else:
                st+=s[i]
        return (st)