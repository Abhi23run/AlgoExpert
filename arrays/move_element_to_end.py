def moveElementToEnd(array, toMove):
    # Write your code here.
    # Not in place (O(N) memory solution)
    final_list=[]
    for item in array:
      if item==toMove:
        pass
      else:
        final_list.append(item)
    n=len(array)
    m=len(final_list)
    final_list+=[toMove]*(n-m)
    return final_list
