# https://leetcode.com/problems/3sum

nums = [-1, 0, 1, 2, -1, -4]
solution = dict()
nums = sorted(nums)
print(nums)

for i in range(len(nums)):
    j, k = 0, len(nums)-1


    while j < i < k:
        print('j is: {}, i is {}, k is {}'.format(j,i,k))
        vals = (nums[j], nums[i], nums[k])
        print(vals)
        s = sum(vals)
        print(s)
        if s == 0:
            solution[vals] = True
        if s < 0:
            j += 1
        else:
            k -= 1
#             print('k changed to {}'.format(k))


    print('-'*40)

print(solution.keys())