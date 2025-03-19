# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        arr=[]
        if k>len(nums):
            k=k%len(nums)
        for i in range(len(nums)-1,len(nums)-k-1,-1):
            el=nums.pop(i)
            arr.append(el)
        nums.reverse()
        for i in arr:
            nums.append(i)
        nums.reverse()