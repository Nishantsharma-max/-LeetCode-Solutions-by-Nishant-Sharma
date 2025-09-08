# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.




class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxdiff=[1]
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    if maxdiff[0]<j-i:
                        maxdiff[0]=j-i
        return maxdiff[0]
        