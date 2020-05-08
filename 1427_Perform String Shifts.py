#--
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


##---- fancy solution
class Solution:
    def stringShift(self, string: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            amount %= len(string)
            if direction == 0:
                # Move necessary amount of characters from start to end
                string = string[amount:] + string[:amount]
            else:
                # Move necessary amount of characters from end to start
                string = string[-amount:] + string[:-amount]
        return string