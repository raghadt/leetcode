class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=height
        left=0
        right=len(a)-1
        mxarea=-1
        while(left<right):
            mxarea = max(mxarea, min(a[left], a[right])*(right-left)  )

        #     print(right)
            if a[left]<a[right]:
                left+=1
            else:
                right-=1

        return (mxarea)