class Solution:
    def productExceptSelf(self, num: List[int]) -> List[int]:
        # num = [1,2,3,4]
        ans1 = [1]
        for i in range(len(num)-1):
            ans1.append(ans1[i]*num[i])

        ans2=[1]
        j=0
        for i in range(len(num)-1, 0, -1):
            # print(ans2)
            ans2.append(ans2[j]*num[i])
            j+=1

        ans2.reverse()
        for i in range(len(num)):
            ans1[i]*=ans2[i]
            
        return ans1