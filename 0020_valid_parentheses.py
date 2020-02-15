class Solution:
    def isValid(self, s: str) -> bool:
        par=s


        if len(par)==1:
            return False
        elif len(par)==0:
            return True
        
        par_dic = {}
        par_dic['}']='{'
        par_dic[')']='('
        par_dic[']']='['
        stack=[]
        for i in range(len(par)):
        #     print(stack[-1])
            stack.append(par[i])
        #     if stack[-1]  in par_dic.keys():
        #         print(par_dic[stack[-1]])

            if stack[-1]  in par_dic.keys() and len(stack)>1 and stack[-2] == par_dic[stack[-1]]:
                stack.pop()
                stack.pop()

        if len(stack)==0:
            return True
        else:
            return False





        #         else:
        #     if i not in par_dic.keys():
        #         stack.append(i)
        #     else:
        #         stack.pop(i)