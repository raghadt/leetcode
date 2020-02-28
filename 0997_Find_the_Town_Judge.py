#-- Time: O(N+E)
#-- Space: O(N)

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
             return -1
        outbound = [0] * N
        inbound = [0] * N

        for a, b in trust:
            # print(a-1)
            outbound[a-1] += 1
            inbound[b-1] +=1


        for i in range(N):
            if outbound[i]==0 and inbound[i]== N-1:
                return (i+1)
        return -1



#----------- using 1 array
#----------- which is smarter tbh

trust_scores = [0] * (N + 1)
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        for a, b in trust:
            trust_scores[a] -= 1
            trust_scores[b] += 1

        for i, score in enumerate(trust_scores[1:], 1):
        #     print(score)
            if score == N - 1:
                return i
        return -1