class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        val = self.queue[0]
        del self.queue[0]
        return val
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.queue)==0:
            return -1
        else: return self.queue[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.queue)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()