# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



#  Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000


# def rotate(matrix):
#      result=[]
#      rev=matrix.reverse()
#      for i in range(len(matrix[0])):
#           row=[]
#           for j in matrix:
#                row.append(j[i])
#           result.append(row)
#      for i in range(len(result)):
#           matrix.pop(0)
#           matrix.append(result[i])
#      return matrix
          
def rotate(matrix):
     matrix.reverse()
     lr=len(matrix[0])
     lc=len(matrix)
     for i in range(lc):
          for j in range(lr):
               matrix[j].append(matrix[i][j])
          for j in range(lr):
               matrix[i].pop(0)
     return matrix

     
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

