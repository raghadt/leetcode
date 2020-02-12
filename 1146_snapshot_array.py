class SnapshotArray:

    def __init__(self, length: int):
        self.active = {}
        self.snaps = []


        return

    def set(self, index: int, val: int) -> None:
        self.active[index]=val
        return
    
    def snap(self) -> int:
        self.snaps.append(self.active.copy())
        # self.snap_counter+=1

        return len(self.snaps)-1

    def get(self, index: int, snap_id: int) -> int:
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)