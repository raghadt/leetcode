#https://leetcode.com/problems/two-sum/
nums = [3,3]
target = 6
dics={}
for i,v in enumerate(nums):
    minus_target=(target-v)
    print(minus_target)
    if (minus_target) in dics.keys():
        print([i,dics[minus_target]])
    dics[v]=i