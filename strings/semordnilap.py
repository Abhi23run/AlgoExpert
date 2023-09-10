def semordnilap(words):
    # Write your code here.
    ans=[]
    s=set()
    for i in words:
      if i[::-1] not in s:
        s.add(i)
      else:
        ans.append([i,i[::-1]])

    return ans
