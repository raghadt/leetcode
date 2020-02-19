
#---------- 5% looool
class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.m = []
        self.size=size

    def next(self, val: int) -> float:
        self.m.append(val)
        if len(self.m)>self.size:
            self.m[:]= self.m[1:]
        return sum(self.m)/len(self.m)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


#------ another solution with Queue

from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.qu = deque()
        self.size=size
        self.summation=0
        

    def next(self, val: int) -> float:
        self.qu.append(val)
        self.summation+=val
        if len(self.qu)>self.size:
            self.summation -= self.qu.popleft()
        return (self.summation)/len(self.qu)



