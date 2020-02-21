class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        # n=19
        found=False
        j=0
        while not found:
            lis=[]
            # print
            for i in str(n):
                lis.append(int(i)**2)
                # print(lis)
            if sum(lis)==1:
                return True
            else:
                prev_len= (len(seen))
                seen.add(sum(lis))
                if len(seen)==prev_len:
                    return False
                n= str(sum(lis))
                # print(n)
                lis = []

