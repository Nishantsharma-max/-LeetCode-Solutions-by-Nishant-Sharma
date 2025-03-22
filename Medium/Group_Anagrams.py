# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

def groupAnagrams(strs):
     result=[]
     meo=[]
     for i in range(len(strs)):
          l1=[j for j in strs[i]]
          l1.sort()
          meo.append("".join(l1))
     for i in range(len(meo)):
          l=[]
          for j in range(len(meo)):
               if meo[i]==meo[j]:
                    l.append(strs[j])
          result.append(l)
     res=[]
     for i in result:
          if i not in res:
               res.append(i)

     return res


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))