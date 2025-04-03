# 11. Container With Most Water


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.




def maxArea(height):
     max_area=0
     for i in range(len(height)):
          count=1
          for j in range(i+1,len(height)):
               if height[i]>=height[j]:
                    pro=height[j]*(count)
               else:
                    pro=height[i]*(count)
               if pro>max_area:
                    max_area=pro
               count+=1
     return max_area

print(maxArea([1,8,6,2,5,4,8,3,7]))