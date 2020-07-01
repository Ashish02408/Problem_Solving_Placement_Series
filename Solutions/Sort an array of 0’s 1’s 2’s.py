class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c=0
        c1=0
        for i in range(0,len(nums)):
            if nums[i]==0:
                c=c+1
            if nums[i]==1:
                c1=c1+1
        for i in range(0,c):
            nums[i]=0
        for i in range(c,(c+c1)):
            nums[i]=1
        for i in range((c+c1),len(nums)):
            nums[i]=2
        print(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        
