# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

# Return the maximum difference. If no such i and j exists, return -1.



# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         maxDiff=[-1]
#         for i in range(len(nums)):
#             for j in range (i+1,len(nums)):
#                 if nums[j]>nums[i]:
#                     if maxDiff[-1]<nums[j]-nums[i]:
#                         maxDiff.append(nums[j]-nums[i])
#         return maxDiff[-1]
        

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff=[-1]
        smallest=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>smallest:
                if maxDiff[-1]<nums[i]-smallest:
                    maxDiff.append(nums[i]-smallest)
            else:
                smallest=nums[i]
                continue
        return maxDiff[-1]