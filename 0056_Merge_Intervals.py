
#-- Time: O(nlogn)
#-- space: O(n)s

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals=[[1,3],[2,6],[8,10],[15,18]]
        intervals.sort(key=lambda x: x[0])
        new_int = []
        found=False
        for interval in intervals:
            if not new_int or new_int[-1][1] < interval[0]:
                new_int.append(interval)
            else:
                # print(new_int)
                new_int[-1][1] = max(new_int[-1][1], interval[1])

        return new_int