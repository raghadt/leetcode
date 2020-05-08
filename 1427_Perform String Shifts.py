class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s_list = list(s)
        for i in shift:

            if i[0]==0:
                val = (s_list[:i[1]])
                del s_list[:i[1]]
                s_list[:] =s_list+ val 
            else:
                # print(i[1])
                val = s_list[-i[1]:]
        #         print(val)
                del s_list[-i[1]:]
                s_list[:] = val + s_list
            # print(s_list)


        return "".join(s_list)